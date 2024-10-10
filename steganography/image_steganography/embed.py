import cv2
import numpy as np

def embed_image_in_image(cover_image_path, secret_image_path, output_image_path):
    """Embed one image into another."""
    # Read the cover image and the secret image
    cover_image = cv2.imread(cover_image_path)
    secret_image = cv2.imread(secret_image_path)

    # Resize secret image to fit in the cover image
    secret_image = cv2.resize(secret_image, (cover_image.shape[1], cover_image.shape[0]))

    # Ensure the secret image can be embedded (i.e., has 3 channels)
    if secret_image.shape[2] != 3:
        raise ValueError("Secret image must have 3 channels (RGB).")

    # Embed secret image into cover image by modifying LSBs
    for i in range(cover_image.shape[0]):
        for j in range(cover_image.shape[1]):
            for k in range(cover_image.shape[2]):  # Iterate through RGB channels
                # Modify the least significant bit of the cover image
                cover_image[i][j][k] = (cover_image[i][j][k] & ~1) | (secret_image[i][j][k] >> 7 & 1)

    # Save the modified image
    cv2.imwrite(output_image_path, cover_image)
