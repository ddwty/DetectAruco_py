# DetectAruco_py

## Description
DetectAruco_py is a Python-based project that utilizes the OpenCV library's ArUco module for detecting the 6D pose of ArUco markers. This application is designed for ease of use on computers without a Python environment setup. The project includes a calibration tool for camera calibration and compiles into an executable using PyInstaller, available in the `dist` directory for straightforward deployment.

## Features
- **Aruco Marker Detection**: Detects Aruco markers and calculates their 6D pose using OpenCV.
- **Camera Calibration**: Includes a calibration script for setting up and calibrating the camera.
- **Standalone Executable**: Compiled with PyInstaller for ease of use without needing a Python environment.
- **Network Integration**: Sends detected 6D pose data to a network socket at port 12345.

## Getting Started
### Prerequisites
- Download the executable from the `dist` folder.
- No Python environment setup is required for running the executable.

### Usage
- **DetectAruco.py**: For detecting Aruco markers.
- **Calibration.py**: For calibrating your camera.

### Camera Calibration
- Run `calibration.py` to calibrate the camera before using the marker detection feature.
- Follow the on-screen instructions to complete the calibration.

