import cv2
from utils import binary_to_text, text_to_binary

def extract_text_from_image(image_path):
    """Extract text from the image."""
    # Read the image
    image = cv2.imread(image_path)

    binary_text = ''
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(image.shape[2]):  # Iterate through RGB channels
                binary_text += str(image[i][j][k] & 1)

    # Split binary text by end marker (##)
    end_marker = text_to_binary('##')
    binary_text_parts = binary_text.split(end_marker)
    
    # Convert binary back to text until the marker
    extracted_text = binary_to_text(binary_text_parts[0])
    return extracted_text
