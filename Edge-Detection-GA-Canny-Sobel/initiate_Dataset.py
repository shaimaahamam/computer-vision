import cv2
import os

# Function to apply Canny edge detection
def apply_canny(image, lower, upper):
    """
    Applies Canny edge detection on the input image.

    Parameters:
    image (ndarray): Input grayscale image on which Canny edge detection is to be applied.
    lower (int): Lower threshold for the hysteresis procedure in Canny edge detection.
    upper (int): Upper threshold for the hysteresis procedure in Canny edge detection.

    Returns:
    ndarray: Image containing the detected edges.
    """
    edges = cv2.Canny(image, lower, upper)
    return edges

# Function to apply Sobel X and Sobel Y edge detection
def apply_sobel(image):
    """
    Applies Sobel edge detection on the input image.

    Parameters:
    image (ndarray): Input grayscale image on which Sobel edge detection is to be applied.

    Returns:
    ndarray: Image containing the combined edges detected by Sobel X and Sobel Y filters.
    """
    # Apply Sobel filter in the X direction
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  
    # Apply Sobel filter in the Y direction
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  
    # Combine the two Sobel results
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)
    # Normalize result to the range of 0-255
    sobel_combined = cv2.convertScaleAbs(sobel_combined)     
   
    return sobel_combined

def process_images_initiate_dataset(input_folder, method, lower=None, upper=None):
    """
    Processes images in the specified input folder using the specified edge detection method 
    and saves the results to an output folder.

    Parameters:
    input_folder (str): Path to the folder containing input images.
    method (str): The edge detection method to apply ('canny', 'sobel', or 'canny_sobel').
    lower (int, optional): Lower threshold for Canny edge detection (required if method is 'canny' or 'canny_sobel').
    upper (int, optional): Upper threshold for Canny edge detection (required if method is 'canny' or 'canny_sobel').

    Returns:
    None: The function saves the processed images to the output folder.
    """
    # Create output folder based on the selected method
    output_folder = os.path.join(method)
    
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is an image
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            # Load the image in grayscale
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Apply the selected edge detection method
            if method == "canny":
                result = apply_canny(image, lower, upper)
            elif method == "sobel":
                result = apply_sobel(image)
            elif method == "canny_sobel":
                edges = apply_canny(image, lower, upper)
                result = apply_sobel(edges)
            else:
                raise ValueError("Invalid method. Choose 'canny', 'sobel', or 'canny_sobel'.")

            # Save the processed image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, result)

            print(f"Processed and saved: {output_path}")

# Define the input folder containing dataset
# Note: I use the sample dir as a dataset dir
input_folder = "computer-vision/Edge-Detection-GA-Canny-Sobel/samples"

# Process images using different edge detection methods
process_images_initiate_dataset(input_folder, method="canny", lower=40, upper=130)
process_images_initiate_dataset(input_folder, method="sobel")
process_images_initiate_dataset(input_folder, method="canny_sobel", lower=40, upper=130)
