# Parking Space Detection System

This project implements a parking space detection system that allows users to manually mark parking spaces on an image and then detect available and occupied spaces in a video feed. The system uses OpenCV for image processing and real-time detection.

## Table of Contents
- [Usage](#usage)
  - [Marking and Detecting Parking Spaces](#marking-and-detecting-parking-spaces)
- [Features](#features)
- [Code Structure](#code-structure)
- [Requirements](#requirements)

## Usage

### Marking and Detecting Parking Spaces
1. Run the `main.py` script to open an image window for marking parking spaces.
2. Left-click to mark the top-left corner of a parking space.
3. Right-click to remove a marked space "not immediately but will be affected"
4. Press 'q' to exit the marking window. The positions will be saved to a file named `carParkPoses`.
5. The program will then proceed to analyze the video feed
6. Green rectangles indicate available spaces, while red rectangles indicate occupied spaces.
7. The count of free spaces will be displayed on the video feed.
8. Press 'q' to exit the video display.

## Features
- Manual marking of parking spaces using mouse events.
- Real-time detection of free and occupied parking spaces from a video feed.
- Visual feedback with colored rectangles representing space availability.
- Saves marked parking positions for future use.

## Code Structure
- `main.py`: A single script for marking parking spaces on an image and detecting them in a video feed.
- `carParkPoses`: A pickle file storing the marked parking positions.
- `image.png`: An image file used for marking parking spots.
- `parking.mp4`: A video file used for detecting parking space availability.

## Requirements
- Python 3.x
- OpenCV 
- pickle

Make sure to have your video file (`carPark.mp4`) and image file (`img.png`) in the same directory as the script for proper functioning.
