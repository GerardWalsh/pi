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

# Build from source
cd ~/opencv && mkdir build && cd build && 
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D CMAKE_SHARED_LINKER_FLAGS=-latomic \
    -D BUILD_EXAMPLES=OFF ..

# Build library
make -j4

# Install library
sudo make install && sudo ldconfig

# Create symlinks
cd /usr/local/lib/python3.7/site-packages/cv2/python-3.7 && sudo mv cv2.cpython-37m-arm-linux-gnueabihf.so cv2.so && cd ~/.virtualenvs/cv/lib/python3.7/site-packages/ && ln -s /usr/local/lib/python3.7/site-packages/cv2/python-3.7/cv2.so cv2.so