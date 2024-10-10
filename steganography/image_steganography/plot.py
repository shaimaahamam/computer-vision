import matplotlib.pyplot as plt

def plot_images(cover_image_path, secret_image_path, stego_image_path, extracted_secret_image_path):
    """Plot the cover image, secret image, stego image, and extracted secret image side by side."""
    # Load images
    cover_image = plt.imread(cover_image_path)
    secret_image = plt.imread(secret_image_path)
    stego_image = plt.imread(stego_image_path)
    extracted_secret_image = plt.imread(extracted_secret_image_path)

    # Create a figure to hold the images
    plt.figure(figsize=(14, 7))

    # Plot cover image
    plt.subplot(1, 4, 1)
    plt.imshow(cover_image)
    plt.title('Cover Image')
    plt.axis('off')

    # Plot secret image
    plt.subplot(1, 4, 2)
    plt.imshow(secret_image)
    plt.title('Secret Image')
    plt.axis('off')

    # Plot stego image
    plt.subplot(1, 4, 3)
    plt.imshow(stego_image)
    plt.title('Stego Image')
    plt.axis('off')

    # Plot extracted secret image
    plt.subplot(1, 4, 4)
    plt.imshow(extracted_secret_image)
    plt.title('Extracted Secret Image')
    plt.axis('off')

    # Show the plot
    plt.tight_layout()
    plt.show()
