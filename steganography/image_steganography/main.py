from embed import embed_image_in_image
from extract import extract_image_from_image
from plot import plot_images

def main():
    cover_image_path = 'images/cover_image.jpg'  
    secret_image_path = 'images/secret_image.png'  
    stego_image_path = 'images/output_image.png'  
    extracted_secret_image_path = 'images/extracted_secret_image.png'  

    # Embed the secret image in the cover image
    embed_image_in_image(cover_image_path, secret_image_path, stego_image_path)

    # Extract the secret image from the modified image
    extract_image_from_image(stego_image_path, extracted_secret_image_path)

    # Plot the cover, secret, stego, and extracted secret images
    plot_images(cover_image_path, secret_image_path, stego_image_path, extracted_secret_image_path)

if __name__ == "__main__":
    main()
