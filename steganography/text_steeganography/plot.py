import matplotlib.pyplot as plt

def plot_images(original_image_path, embedded_image_path):
    """Plot the original and modified images side by side."""
    # Load images
    original_image = plt.imread(original_image_path)
    modified_image = plt.imread(embedded_image_path)

    # Create a figure to hold the images
    plt.figure(figsize=(7, 7))

    # Plot original image
    plt.subplot(1, 2, 1)
    plt.imshow(original_image)
    plt.title('Original Image')
    plt.axis('off')

    # Plot embedded image
    plt.subplot(1, 2, 2)
    plt.imshow(modified_image)
    plt.title('Embedded Image')
    plt.axis('off')

    # Show the plot
    plt.tight_layout()
    plt.show()
