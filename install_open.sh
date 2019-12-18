#!/bin/bash

# Remove & create disk space 
sudo apt-get purge wolfram-engine libreoffice* -y && sudo apt-get clean -y && sudo apt-get autoremove -y

# Update
sudo apt-get update && sudo apt-get upgrade -y

# Install CMake (for C++ development)
sudo apt-get install build-essential cmake pkg-config -y

# Install libraries for media formats
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev -y

# Install GUI libraries
sudo apt-get install libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev -y 

# Optimization libraries
sudo apt-get install libatlas-base-dev gfortran -y 

# Big data filesystem hdf5 (forDL)/ Qt GUI
sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103 libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5 -y

# Install OpenCV from source
cd ~ && wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.1.zip && wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.1.zip && unzip opencv.zip && unzip opencv_contrib.zip && mv opencv-4.1.1 opencv && mv opencv_contrib-4.1.1 opencv_contrib