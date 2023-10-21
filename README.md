# Number-Plate-detection
Number Plate Recognition System uses the concept of Optical character Recognition (OCR) to read the characters of a vehicle license plate.In other words ,LPR takes the image of a vehicle as input and outputs the characters written on its license plate.

This Python script uses the OpenCV and Tesseract libraries for License Plate Recognition (LPR). The program reads an image of a car, processes it to identify the license plate, extracts the license plate number, and writes the result to an Excel file.

## Prerequisites

- Python 3.x
- OpenCV (`cv2`) library
- Imutils library (`imutils`)
- Tesseract OCR engine
- Pytesseract library (`pytesseract`)
- Xlsxwriter library (`xlsxwriter`)

### Installing Dependencies

```bash
pip install opencv-python imutils pytesseract xlsxwriter
Ensure Tesseract OCR is installed and the path is set correctly. You can download Tesseract OCR from https://github.com/tesseract-ocr/tesseract.

Usage
Clone the repository or download the script.

Ensure all dependencies are installed.

Update the path to the Tesseract OCR engine in the script (replace "C:\Program Files\Tesseract-OCR\tesseract.exe").


Copy code
python license_plate_recognition.py
Output
The script will display various stages of image processing, such as the original image, grayscale image, smoothed image, edges, and contours.
The final result will show the identified contours and the extracted license plate number.
The cropped license plate image will be displayed, and the extracted license plate number will be printed to the console.
The license plate number will be written to an Excel file named out.xlsx.
