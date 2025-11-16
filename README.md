# Automatic Number Plate Recognition with Python and YOLOv8

![ANPR Demo](https://img.shields.io/badge/Project-ANPR%20System-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-4.7-red)

A robust Automatic Number Plate Recognition (ANPR) system that detects vehicles, tracks them across frames, and recognizes license plate text using YOLOv8 for detection and EasyOCR for text recognition.

## 🚀 Features

- **Vehicle Detection**: Uses YOLOv8 pre-trained model to detect vehicles
- **License Plate Detection**: Custom YOLOv8 model for accurate license plate detection
- **Vehicle Tracking**: SORT algorithm for tracking vehicles across frames
- **Text Recognition**: EasyOCR for license plate text recognition
- **Data Interpolation**: Handles missing frames with interpolation
- **Visualization**: Generates annotated video with bounding boxes and text

## 📁 Project Structure
automatic-number-plate-recognition-python-yolov8/
├── main.py # Main detection and tracking script
├── util.py # Utility functions for OCR and CSV writing
├── visualize.py # Visualization script for results
├── add_missing_data.py # Interpolation for missing frames
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
├── models/ # Directory for model files
├── sort/ # SORT tracking algorithm
└── README.md # Project documentation

text

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/GuptaRaj007/automatic-number-plate-recognition-python-yolov8.git
cd automatic-number-plate-recognition-python-yolov8
Create virtual environment (Recommended)

bash
python -m venv myenv
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Setup SORT tracker

bash
# The sort directory is already included in this repository
# No additional setup required
Download Model Files

Download yolov8n.pt from Ultralytics YOLOv8

Download license_plate_detector.pt from the original author's Patreon

Place both model files in the models/ directory

🎯 Usage
1. Run Detection and Tracking
bash
python main.py
This will:

Process the video frame by frame

Detect vehicles and license plates

Track vehicles across frames

Recognize license plate text

Generate test.csv with results

2. Interpolate Missing Data
bash
python add_missing_data.py
This fills in missing frames using interpolation and generates test_interpolated.csv

3. Visualize Results
bash
python visualize.py
Creates out.mp4 - an annotated video with:

Green bordered boxes around vehicles

Red rectangles around license plates

License plate crops displayed above vehicles

Recognized license plate text

📊 Output Files
test.csv - Raw detection results

test_interpolated.csv - Results with interpolated frames

out.mp4 - Visualized output video with annotations

🔧 Configuration
Video Input
Update the video path in main.py:

python
cap = cv2.VideoCapture('your_video.mp4')
Vehicle Classes
Modify vehicle classes in main.py:

python
vehicles = [2, 3, 5, 7]  # COCO dataset classes: car, motorcycle, bus, truck
🛠️ Dependencies
ultralytics==8.0.114 - YOLOv8 for object detection

opencv-python==4.7.0.72 - Computer vision operations

pandas==2.0.2 - Data manipulation

numpy==1.24.3 - Numerical operations

easyocr==1.7.0 - Text recognition

scipy==1.10.1 - Scientific computing

filterpy==1.4.5 - Kalman filters for tracking

🎥 Sample Video
The sample video used in this project can be downloaded from Pexels.

🔍 How It Works
Vehicle Detection: YOLOv8 detects vehicles in each frame

Tracking: SORT algorithm tracks vehicles across frames

License Plate Detection: Custom YOLOv8 model detects license plates

Text Recognition: EasyOCR reads text from detected license plates

Data Association: License plates are associated with corresponding vehicles

Interpolation: Missing data is filled using linear interpolation

Visualization: Results are overlaid on the original video

🐛 Troubleshooting
Common Issues
Memory Error:

Reduce video resolution

Process shorter video segments

Model Not Found:

Ensure model files are in models/ directory

Check file names match the code

Video Not Playing:

Use VLC Media Player for best compatibility

Check if output file was created successfully

Performance Tips
Use GPU for faster processing (install CUDA-enabled PyTorch)

Reduce video resolution for faster processing

Process shorter video segments for testing

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is for educational purposes. Please respect the licenses of the included components:

YOLOv8: AGPL-3.0

SORT: MIT

EasyOCR: Apache 2.0

🙏 Acknowledgments
Ultralytics for YOLOv8

abewley for SORT tracker

Jaided AI for EasyOCR

Computer Vision Engineer for the original tutorial and license plate model

📞 Contact
Raj Gupta - GitHub

Project Link: https://github.com/GuptaRaj007/automatic-number-plate-recognition-python-yolov8

Note: This project is intended for educational and research purposes. Please ensure compliance with local laws and regulations when using ANPR systems.


