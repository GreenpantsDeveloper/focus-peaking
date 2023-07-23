# Focus Peaking in Python

## 1. Introduction

This project implements a focus peaking algorithm in Python using the OpenCV library. Focus peaking is a technique used
in photography, videography and image processing to highlight in-focus areas in an image. The algorithm detects edges or
regions with significant changes in intensity, which usually correspond to in-focus regions in the image.

By installing and running this project, you can check out focus peaking on one of the video streaming devices (e.g.
webcam) attached to your machine.

## 2. Installation

To run this project, you first need to have Python installed on your system. This project was developed for Python 3.9
and tested on an M1 Macbook. You can install the required libraries using pip (consider using a virtual environment):

```bash
pip install -r requirements.txt
```

## 3. How to run

1. Clone the repository to your local machine.

2. Ensure you have Python and the required libraries installed.

3. Customize the config.ini file to adjust parameters like camera index, threshold, and blur kernel size.

```ini
[Camera]
Index = 0

[FocusPeaking]
Threshold = 100
BlurKernelSize = (5, 5)
```

* **Camera > Index**: set the camera index to use for the webcam stream. By default, it's set to 0, which represents the
  device's default camera.
* **FocusPeaking > Threshold**: adjust the sensitivity of edge detection. Higher values make the algorithm more
  sensitive to edges.
* **FocusPeaking > BlurKernelSize**: customize the size of the Gaussian blur kernel used for noise reduction. The format
  is (width, height).

4. Execute the main Python script:

```bash
python focus_peaking.py
```

5. A window will appear showing the webcam stream with focus peaking applied.

6. Press 'q' to exit the application.

## 4. Background

This focus peaking algorithm works based on the concept of image gradients. It involves the following steps:

1. **Grayscale conversion**: the input image or frame from the webcam is first converted to grayscale, to simplify edge
   detection.

2. **Smoothing**: a Gaussian blur is applied to the grayscale image to reduce noise and make the subsequent edge
   detection more accurate.

3. **Gradient Calculation**: the gradient magnitude of the smoothed image is calculated using the Sobel operators. The
   gradient
   magnitude represents the strength of edges in the image.

4. **Thresholding**: the gradient magnitude is thresholded to obtain a binary image, where edges are represented as
   white pixels and non-edges as black pixels. The threshold value is user-adjustable.

5. **Highlighting**: the binary edge map is combined with the original frame, and in-focus areas are highlighted by
   applying a red color to the corresponding pixels.

## 5. Future Improvements

This project provides a basic implementation of focus peaking. For further improvements, consider the following:

1. Incorporate user interaction to adjust parameters (focus, exposure, etc.) in real-time while the application is
   running.

2. Implement more edge detection algorithms, e.g. Canny edge detection, to enhance accuracy and adaptability
   to various image conditions.

3. Develop a graphical user interface (GUI) to make the application more user-friendly and accessible.

4. Explore ways to optimize the algorithm's performance for real-time processing of high-resolution video streams.

## 6. Conclusion

This implementation of focus peaking demonstrates the application of computer vision techniques to enhance image
processing in photography and videography. By detecting in-focus areas, the algorithm can aid creators in capturing
sharper and more visually appealing images. This project serves as a starting point for a better understanding of focus
peaking, as well as a baseline for focus peaking implemented in Python.