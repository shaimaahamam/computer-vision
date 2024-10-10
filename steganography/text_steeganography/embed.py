import cv2
from utils import text_to_binary

def embed_text_in_image(image_path, text, output_image_path):
    """Embed text into the image"""
    
    image = cv2.imread(image_path)

    # Convert text to binary and append end marker (##)
    text_with_marker = text + '##'
    binary_text = text_to_binary(text_with_marker)

    data_index = 0
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(image.shape[2]):  # Iterate through RGB channels
                if data_index < len(binary_text):
                    # Modify the least significant bit
                    image[i][j][k] = (image[i][j][k] & ~1) | int(binary_text[data_index])
                    data_index += 1

    # Save the modified image
    cv2.imwrite(output_image_path, image)
