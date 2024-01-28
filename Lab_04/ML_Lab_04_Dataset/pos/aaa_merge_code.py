import glob
import numpy as np

def create_array_of_array_from_text_files():
    """Creates an array of array, where each entry contains the content of each of the text files in the current folder.

    Returns:
        numpy.ndarray: An array of array, where each entry contains the content of each of the text files in the current folder.
    """

    text_files = glob.glob("*.txt")

    array_of_array = []
    for text_file in text_files:
        with open(text_file, "r") as f:
            text = f.read()

        # Split the text into lines.
        lines = text.split("\n")

        # Add the lines to the array of array.
        array_of_array.append(lines)

    return np.array(array_of_array)

# Create the array of array.
array_of_array = create_array_of_array_from_text_files()

# Print the shape of the array of array.
print(array_of_array.shape)

# Print the first 10 elements of the array of array.
print(array_of_array[:10])
