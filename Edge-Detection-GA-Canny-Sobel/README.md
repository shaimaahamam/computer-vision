# Edge Detection Optimization using Genetic Algorithms (GA)

This project utilizes Genetic Algorithms (GA) to optimize parameters for **Canny edge detection** and applies **Sobel filters** for detecting edges in images. The goal is to find the most frequent optimal lower and upper threshold values for Canny edge detection across multiple images. 


## Features
- **GA Optimization for Canny:** Runs a Genetic Algorithm to find optimal thresholds (lower and upper) for Canny edge detection.
- **Edge Detection Methods:**
  - **Canny:** Applies the Canny edge detection algorithm.
  - **Sobel:** Applies Sobel edge detection in both X and Y directions and combines the results.
  - **Canny + Sobel:** Applies Canny edge detection first, then uses Sobel on the result.
- **Batch Processing:** Processes images in batches from the specified folder, detects edges, and saves results.

## File Structure

Edge-Detection-GA-Canny-Sobel/

    │
    ├── dataset/                 
    │   ├── image1.jpg
    │   └── image2.png
    │
    ├── samples/                 
    │   ├── image1.jpg
    │   └── image2.png
    │
    ├── Canny_params_GA.py               
    └── initiate_Dataset.py              

The project consists of two main Python files:
- `Canny_params_GA.py`: Implements the GA to optimize the thresholds for Canny edge detection.
- `initiate_Dataset.py`: Applies the selected edge detection method (Canny, Sobel, or both) on all images in  
                        the folder with the the threshold values that came from last process.


## How It Works

### 1. GA-based Canny Edge Detection (`Canny_params_GA.py`)
This script defines and runs a Genetic Algorithm to optimize the thresholds for Canny edge detection:
- **Fitness Function:** The fitness value is based on the number of edge pixels detected by Canny.
- **GA Parameters:** 
  - **Population:** 20 individuals.
  - **Generations:** 10.
  - **Crossover and Mutation:** Used to evolve the population and improve the thresholds.
- **Input Folder:** It processes all images in the folder and identifies the most frequent lower and upper Canny thresholds across all images.


### 2. Edge Detection Methods (`initiate_Dataset.py`)
This script allows users to apply different edge detection methods on the images:
- **Canny:** Requires optimal thresholds found by the GA or user-defined ones.
- **Sobel:** Detects edges in both X and Y directions.
- **Canny + Sobel:** Combines the two techniques.

It processes each image in the folder, applies the chosen method, and saves the result in the folder with the name of method applied.


