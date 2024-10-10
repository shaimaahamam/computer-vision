from embed import embed_text_in_image
from extract import extract_text_from_image
from plot import plot_images

def main():
    image_path = 'images/cover_image.jpg' 
    output_image_path = 'images/output_image.png'  
    text_message = 'This is an image steganography project'

    # Embed the text in the image
    embed_text_in_image(image_path, text_message, output_image_path)

    # Plot embedded image after embedding text
    plot_images(image_path, output_image_path)

    # Extract the text from the modified image
    extracted_text = extract_text_from_image(output_image_path)
    print('Extracted Text:', extracted_text)

if __name__ == "__main__":
    main()
