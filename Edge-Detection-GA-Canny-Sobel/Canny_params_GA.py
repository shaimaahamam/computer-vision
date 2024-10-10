import cv2
import numpy as np
import os
from deap import base, creator, tools, algorithms
from collections import Counter

# Define the fitness function for GA
def fitness(individual, image):
    """
    Fitness function for evaluating the quality of edge detection.
    
    Parameters:
    individual (list): A list containing two values [lower, upper] representing 
                       the Canny edge detection thresholds.
    image (ndarray): The input grayscale image on which edge detection is performed.
    
    Returns:
    tuple: A single-element tuple containing the fitness value, which is the sum 
           of the detected edge pixels (indicating the quantity/quality of edges detected).
    """
    lower, upper = individual
    
    # Apply Canny edge detection using the provided lower and upper thresholds
    edges = cv2.Canny(image, lower, upper)
    
    # Calculate fitness as the sum of edge pixels (proxy for edge detection quality)
    fitness_value = np.sum(edges)
    
    # Return fitness as a tuple (required by DEAP framework)
    return fitness_value,

# Setup GA
def setup_ga(image):
    """
    Sets up the Genetic Algorithm (GA) by defining the individual representation,
    population, operators (crossover, mutation, selection), and the fitness function.
    
    Parameters:
    image (ndarray): The input grayscale image on which GA will optimize edge detection.
    
    Returns:
    toolbox (deap.base.Toolbox): The configured DEAP toolbox with registered GA operators.
    """
    # Define custom classes for GA fitness and individual (if not already defined)
    if not hasattr(creator, "FitnessMax"):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    if not hasattr(creator, "Individual"):
        creator.create("Individual", list, fitness=creator.FitnessMax)

    # Initialize DEAP toolbox to register genetic algorithm operators
    toolbox = base.Toolbox()
    
    # Register attribute generators for lower and upper thresholds for Canny
    toolbox.register("attr_lower", np.random.randint, 50, 150)  # Random lower threshold
    toolbox.register("attr_upper", np.random.randint, 150, 250)  # Random upper threshold
    
    # Define an individual as a list with two attributes (lower, upper)
    toolbox.register("individual", tools.initCycle, creator.Individual,
                     (toolbox.attr_lower, toolbox.attr_upper), n=1)
    
    # Define the population as a list of individuals
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Register the fitness evaluation function
    toolbox.register("evaluate", fitness, image=image)
    
    # Register genetic operators
    toolbox.register("mate", tools.cxBlend, alpha=0.5)  # Crossover (blend two parents)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=5, indpb=0.2)  # Mutation
    toolbox.register("select", tools.selTournament, tournsize=3)  # Selection
    
    return toolbox

# Run GA on a single image
def run_ga(image):
    """
    Runs the Genetic Algorithm (GA) on a single grayscale image to optimize the Canny 
    edge detection thresholds.
    
    Parameters:
    image (ndarray): The input grayscale image to optimize.
    
    Returns:
    best_individual (list): The best individual (thresholds) found by the GA.
    """
    # Setup the GA toolbox with the image-specific fitness function
    toolbox = setup_ga(image)
    
    # Initialize the population with 20 individuals
    population = toolbox.population(n=20)
    
    # Run the Genetic Algorithm for 10 generations
    algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.2, ngen=10, verbose=False)
    
    # Select and return the best individual (the one with the highest fitness)
    best_individual = tools.selBest(population, k=1)[0]
    
    return best_individual

# Function to bin values into ranges
def bin_values(values, bin_size):
    """
    Bins the values into ranges of the specified bin size.
    
    Parameters:
    values (list): A list of numeric values to be binned.
    bin_size (int): The size of the bins.
    
    Returns:
    list: A list of binned values where each value is rounded down to the nearest bin.
    """
    binned_values = [int(v // bin_size) * bin_size for v in values]
    return binned_values

# Function to get the most common value in bins
def most_common_in_bins(values, bin_size):
    """
    Finds the most common value in the binned values.
    
    Parameters:
    values (list): A list of numeric values.
    bin_size (int): The size of the bins to group values.
    
    Returns:
    int: The most common value in the binned list of values.
    """
    # Bin the values using the specified bin size
    binned_values = bin_values(values, bin_size)
    
    # Use Counter to find the most common binned value
    most_common = Counter(binned_values).most_common(1)[0][0]
    
    return most_common

# Function to process all images in a folder and get the optimal parameters
def process_images_in_folder(folder_path):
    """
    Processes all images in the specified folder, runs the GA on each image to find 
    the optimal Canny edge detection thresholds, and identifies the most common thresholds.
    
    Parameters:
    folder_path (str): The path to the folder containing image files.
    
    Returns:
    None: Prints the most frequent lower and upper Canny thresholds across all images.
    """
    lowers = []
    uppers = []
    
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an image
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            
            # Load the image as grayscale
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            
            # Run GA on the image to get the best Canny thresholds
            best_solution = run_ga(image)
            
            # Extract the best lower and upper thresholds from the solution
            lower, upper = best_solution
            lowers.append(lower)
            uppers.append(upper)
    
    # Bin the results and find the most common lower and upper thresholds
    bin_size = 10
    best_lower = most_common_in_bins(lowers, bin_size)
    best_upper = most_common_in_bins(uppers, bin_size)

    # Print the most frequent lower and upper Canny thresholds across all images
    print(f"Most frequent Canny lower threshold: {best_lower}")
    print(f"Most frequent Canny upper threshold: {best_upper}")

# Run the function
folder_path = "computer-vision/Edge-Detection-GA-Canny-Sobel/samples"
process_images_in_folder(folder_path)
