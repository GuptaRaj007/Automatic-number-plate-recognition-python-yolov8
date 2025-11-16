import ast
import cv2
import numpy as np
import pandas as pd


def draw_border(img, top_left, bottom_right, color=(0, 255, 0), thickness=10, line_length_x=200, line_length_y=200):
    x1, y1 = top_left
    x2, y2 = bottom_right

    cv2.line(img, (x1, y1), (x1, y1 + line_length_y), color, thickness)  #-- top-left
    cv2.line(img, (x1, y1), (x1 + line_length_x, y1), color, thickness)

    cv2.line(img, (x1, y2), (x1, y2 - line_length_y), color, thickness)  #-- bottom-left
    cv2.line(img, (x1, y2), (x1 + line_length_x, y2), color, thickness)

    cv2.line(img, (x2, y1), (x2 - line_length_x, y1), color, thickness)  #-- top-right
    cv2.line(img, (x2, y1), (x2, y1 + line_length_y), color, thickness)

    cv2.line(img, (x2, y2), (x2, y2 - line_length_y), color, thickness)  #-- bottom-right
    cv2.line(img, (x2, y2), (x2 - line_length_x, y2), color, thickness)

    return img


# Read the results
results = pd.read_csv('./test_interpolated.csv')

# Load video - FIXED PATH
video_path = './2103099-uhd_3840_2160_30fps.mp4'  # Added ./ to make path explicit
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
    print("Please check:")
    print("1. The video file exists in the current directory")
    print("2. The file name matches exactly")
    print("3. The video file is not corrupted")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('./out.mp4', fourcc, fps, (width, height))

license_plate = {}
for car_id in np.unique(results['car_id']):
    max_ = np.amax(results[results['car_id'] == car_id]['license_number_score'])
    license_plate[car_id] = {'license_crop': None,
                             'license_plate_number': results[(results['car_id'] == car_id) &
                                                             (results['license_number_score'] == max_)]['license_number'].iloc[0]}
    
    frame_nmr_to_read = results[(results['car_id'] == car_id) &
                               (results['license_number_score'] == max_)]['frame_nmr'].iloc[0]
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nmr_to_read)
    ret, frame = cap.read()
    
    # Check if frame was read successfully
    if not ret or frame is None:
        print(f"Warning: Could not read frame {frame_nmr_to_read} for car {car_id}")
        continue

    try:
        x1, y1, x2, y2 = ast.literal_eval(results[(results['car_id'] == car_id) &
                                                  (results['license_number_score'] == max_)]['license_plate_bbox'].iloc[0].replace('[ ', '[').replace('   ', ' ').replace('  ', ' ').replace(' ', ','))
        
        # Ensure coordinates are within frame bounds
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(frame.shape[1], x2)
        y2 = min(frame.shape[0], y2)
        
        # Check if crop area is valid
        if x2 > x1 and y2 > y1:
            license_crop = frame[y1:y2, x1:x2, :]
            license_crop = cv2.resize(license_crop, (int((x2 - x1) * 400 / (y2 - y1)), 400))
            license_plate[car_id]['license_crop'] = license_crop
        else:
            print(f"Warning: Invalid crop coordinates for car {car_id}: ({x1}, {y1}, {x2}, {y2})")
            
    except Exception as e:
        print(f"Error processing license plate for car {car_id}: {e}")
        continue


frame_nmr = -1
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# read frames
ret = True
while ret:
    ret, frame = cap.read()
    frame_nmr += 1
    if ret and frame is not None:
        df_ = results[results['frame_nmr'] == frame_nmr]
        for row_indx in range(len(df_)):
            try:
                # draw car
                car_x1, car_y1, car_x2, car_y2 = ast.literal_eval(df_.iloc[row_indx]['car_bbox'].replace('[ ', '[').replace('   ', ' ').replace('  ', ' ').replace(' ', ','))
                draw_border(frame, (int(car_x1), int(car_y1)), (int(car_x2), int(car_y2)), (0, 255, 0), 25,
                            line_length_x=200, line_length_y=200)

                # draw license plate
                x1, y1, x2, y2 = ast.literal_eval(df_.iloc[row_indx]['license_plate_bbox'].replace('[ ', '[').replace('   ', ' ').replace('  ', ' ').replace(' ', ','))
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 12)

                # crop license plate
                car_id = df_.iloc[row_indx]['car_id']
                if car_id in license_plate and license_plate[car_id]['license_crop'] is not None:
                    license_crop = license_plate[car_id]['license_crop']
                    H, W, _ = license_crop.shape

                    try:
                        frame[int(car_y1) - H - 100:int(car_y1) - 100,
                              int((car_x2 + car_x1 - W) / 2):int((car_x2 + car_x1 + W) / 2), :] = license_crop

                        frame[int(car_y1) - H - 400:int(car_y1) - H - 100,
                              int((car_x2 + car_x1 - W) / 2):int((car_x2 + car_x1 + W) / 2), :] = (255, 255, 255)

                        (text_width, text_height), _ = cv2.getTextSize(
                            license_plate[car_id]['license_plate_number'],
                            cv2.FONT_HERSHEY_SIMPLEX,
                            4.3,
                            17)

                        cv2.putText(frame,
                                    license_plate[car_id]['license_plate_number'],
                                    (int((car_x2 + car_x1 - text_width) / 2), int(car_y1 - H - 250 + (text_height / 2))),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    4.3,
                                    (0, 0, 0),
                                    17)

                    except Exception as e:
                        print(f"Error drawing overlay on frame {frame_nmr}: {e}")
                        pass

            except Exception as e:
                print(f"Error processing frame {frame_nmr}, row {row_indx}: {e}")
                continue

        out.write(frame)
        
        # Show progress
        if frame_nmr % 100 == 0:
            print(f"Processed frame {frame_nmr}")

        # frame = cv2.resize(frame, (1280, 720))
        # cv2.imshow('frame', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

out.release()
cap.release()
# cv2.destroyAllWindows()
print("Visualization complete! Output saved as out.mp4")