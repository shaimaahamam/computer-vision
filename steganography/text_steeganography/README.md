# Text Steganography: Embedding and Extracting Text in Images

This project demonstrates how to embed text within an image using the Least Significant Bit (LSB) steganography technique. It also provides functionality for extracting the hidden text from the modified image and visualizing the results, making it an excellent tool for understanding data hiding and image processing.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [How It Works](#how-it-works)



## Features

- **Text Embedding**: Embed a secret text message within an image without significant visible alteration.
- **Text Extraction**: Retrieve the hidden text from the modified image.
- **Visualization**: Plot the original image, the modified image with embedded text, and the extracted text for easy comparison.
- **Cross-Platform**: Works on any platform that supports Python.

## Requirements

- **Python**: Version 3.x
- **OpenCV**: For image processing
- **Matplotlib**: For plotting images

 ## File Structure

steganography/
    text_steganography/
    │
    ├── images
    │   ├── cover_image.jpg          # The image used to hide the secret text
    │   ├── output_image.png         # The resulting image after embedding text
    │   └── extracted_text.txt       # The text extracted from the stego image
    │
    ├── embed.py                     # Contains the function to embed the secret text
    ├── extract.py                   # Contains the function to extract the secret text
    ├── plot.py                      # Contains the function to visualize images
    ├── utils.py                     # Contains utility functions for text conversion
    └── main.py                      # Main script to run the program


## How It Works

Embedding Process:
    The text message is converted into binary representation using the text_to_binary function from the utils.py module.
    The Least Significant Bit of each pixel in the cover image is modified to store the binary data of the text message. This ensures that changes are minimal and not easily detectable.

Extraction Process:
    The modified image is processed to read the LSBs, reconstructing the hidden text using the binary_to_text function from the utils.py module.

Visualization:
    The plot.py module is used to create visual comparisons of the original image and the stego image with embedded text for easy understanding.