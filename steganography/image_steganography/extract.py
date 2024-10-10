import cv2
import numpy as np

def extract_image_from_image(cover_image_path, output_secret_image_path):
    """Extract the hidden image from the cover image."""
    # Read the cover image
    cover_image = cv2.imread(cover_image_path)

    # Prepare an empty array for the extracted image
    height, width = cover_image.shape[:2]
    secret_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Extract the secret image from the cover image by reading LSBs
    for i in range(height):
        for j in range(width):
            for k in range(cover_image.shape[2]):  # Iterate through RGB channels
                # Get the LSB of the cover image channel and scale it to 255
                lsb = cover_image[i][j][k] & 1
                secret_image[i][j][k] = lsb * 255  # Map LSB to either 0 or 255

    # Save the extracted secret image
    cv2.imwrite(output_secret_image_path, secret_image)
