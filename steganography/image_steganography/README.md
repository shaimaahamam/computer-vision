# Image Steganography: Embedding and Extracting Images

This project demonstrates how to embed one image within another using the Least Significant Bit (LSB) steganography technique. It also provides functionality for extracting the hidden image and visualizing the results, making it an excellent tool for understanding image processing and data hiding.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [How It Works](#how-it-works)

## Features

- **Image Embedding**: Embed a secret image within a cover image without significant visible alteration.
- **Image Extraction**: Retrieve the hidden image from the modified stego image.
- **Visualization**: Plot the original cover image, the secret image, the stego image, and the extracted secret image side by side for easy comparison.
- **Cross-Platform**: Works on any platform that supports Python.

## Requirements

- **Python**: Version 3.x
- **OpenCV**: For image processing
- **Matplotlib**: For plotting images



## File Structure


steganography/
    image_steganography/
    
    │
    ├── images
    │   ├── cover_image.jpg          # The image used to hide the secret image
    │   ├── secret_image.png         # The image to be hidden
    │   ├── output_image.png         # The resulting image after embedding
    │   └── extracted_secret_image.png # The image extracted from the stego image
    │
    ├── embed.py                     # Contains the function to embed the secret image
    ├── extract.py                   # Contains the function to extract the secret image
    ├── plot.py                      # Contains the function to visualize images
    └── main.py                      # Main script to run the program


## How It Works

1- Embedding Process:
    The secret image is resized to fit the cover image.
    The Least Significant Bit of each pixel in the cover image is modified to store the pixel data of the secret image. 
    This ensures that changes are minimal and not easily detectable.

2- Extraction Process:
    The stego image is processed to read the LSBs, reconstructing the hidden image.

3- Visualization:
    The plot.py module provides functionality to visually compare the cover image, the secret image, the stego image (the result of embedding), and the extracted secret image. It displays these images side by side, allowing for easy assessment of the embedding process's effectiveness and the fidelity of the extracted data.


