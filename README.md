# Automatic Number Plate Recognition with Python and YOLOv8

![ANPR Demo](https://img.shields.io/badge/Project-ANPR%20System-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-4.7-red)

A complete Automatic Number Plate Recognition (ANPR) system that detects vehicles, tracks them across frames, extracts license plates, and recognizes text using YOLOv8 and EasyOCR.

---

## 🚀 Features

* **Vehicle Detection** using YOLOv8
* **License Plate Detection** using a custom-trained YOLOv8 model
* **Vehicle Tracking** with the SORT algorithm
* **OCR Recognition** with EasyOCR
* **Interpolation** for missing frames
* **Visualization** to generate annotated result videos

---

## 📁 Project Structure

```
automatic-number-plate-recognition-python-yolov8/
│
├── main.py                      # Main detection and tracking
├── util.py                      # OCR and utility functions
├── visualize.py                 # Results visualization
├── add_missing_data.py          # Frame interpolation
├── requirements.txt             # Python dependencies
├── README.md                    # Documentation
│
├── models/                      # Model files (place here)
│   ├── license_plate_detector.pt
│   └── yolov8n.pt
│
└── sort/                        # SORT tracker
    ├── sort.py
    └── __init__.py
```

---

## 🛠️ Installation

### **Prerequisites**

* Python 3.8+
* Git

---

### **1. Clone the repository**

```bash
git clone https://github.com/GuptaRaj007/automatic-number-plate-recognition-python-yolov8.git
cd automatic-number-plate-recognition-python-yolov8
```

---

### **2. Create a virtual environment (recommended)**

```bash
python -m venv myenv
```

Activate it:

**Windows**

```bash
myenv\Scripts\activate
```

**macOS/Linux**

```bash
source myenv/bin/activate
```

---

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

### **4. Set up model files**

* Download **yolov8n.pt** from Ultralytics
* Download **license_plate_detector.pt**
* Place both inside the **models/** folder.

No setup is needed for SORT — it's included.

---

## 🎯 Usage

### **1. Run detection & tracking**

```bash
python main.py
```

This will:

* Read video input
* Detect vehicles
* Detect license plates
* Track vehicles
* Run OCR
* Save results to **test.csv**

---

### **2. Interpolate missing data**

```bash
python add_missing_data.py
```

Generates:

* `test_interpolated.csv`

---

### **3. Visualize results**

```bash
python visualize.py
```

Produces:

* `out.mp4` (annotated video with bounding boxes & text)

---

## 📊 Output Files

| File                      | Description                 |
| ------------------------- | --------------------------- |
| **test.csv**              | Raw detection results       |
| **test_interpolated.csv** | After interpolation         |
| **out.mp4**               | Final rendered output video |

---

## 🔧 Configuration

### **Video Input**

Edit in `main.py`:

```python
cap = cv2.VideoCapture('your_video.mp4')
```

### **Vehicle Classes**

```python
vehicles = [2, 3, 5, 7]   # car, motorcycle, bus, truck
```

---

## 🛠️ Dependencies

* `ultralytics==8.0.114`
* `opencv-python==4.7.0.72`
* `pandas==2.0.2`
* `numpy==1.24.3`
* `easyocr==1.7.0`
* `scipy==1.10.1`
* `filterpy==1.4.5`

---

## 🎥 Sample Video

You can download sample vehicle footage from **Pexels** to test the pipeline.

---

## 🔍 How It Works

1. **YOLOv8 detects vehicles**
2. **SORT tracks vehicles frame-to-frame**
3. **YOLOv8 detects license plates**
4. **EasyOCR extracts plate characters**
5. **Plates are linked to tracked vehicles**
6. **Missing entries are interpolated**
7. **Final video is rendered with annotations**

---

## 🐛 Troubleshooting

### **Memory Issues**

* Lower the input video resolution
* Use shorter clips during testing

### **Model Not Found**

* Ensure `.pt` files are inside `/models`

### **Video Output Not Playing**

* Use VLC Media Player
* Ensure processing completed without errors

### **Performance Tips**

* Use a GPU-enabled machine
* Reduce video resolution
* Process smaller video segments for testing

---

## 🤝 Contributing

Contributions are welcome!

---

## 📝 License

This project is for educational use.
Please respect the original licenses of:

* YOLOv8 — AGPL-3.0
* SORT — MIT
* EasyOCR — Apache 2.0

---

## 🙏 Acknowledgments

* Ultralytics (YOLOv8)
* abewley (SORT)
* Jaided AI (EasyOCR)

---

## 📞 Contact

**Raj Gupta**

* **LinkedIn:** [https://www.linkedin.com/in/raj-gupta-52b39230a/](https://www.linkedin.com/in/raj-gupta-52b39230a/)
* **Email:** [guptaaraj007@gmail.com](mailto:guptaaraj007@gmail.com)
* **Project Link:** [https://github.com/GuptaRaj007/automatic-number-plate-recognition-python-yolov8](https://github.com/GuptaRaj007/automatic-number-plate-recognition-python-yolov8)

---

If you want, I can **polish it even more**, add **badges**, **GIF demo**, or convert it into a **professional portfolio-style README**.
