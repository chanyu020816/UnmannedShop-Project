import os
from PIL import Image

# Directory containing your images
input_directory = "RawImages/"

# Directory to save the resized images
output_directory = "ResizedImages/"

# Target size
target_size = (640, 640)

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok = True)

# List all files in the input directory
files = os.listdir(input_directory)
if __name__ == "__main__":
    for filename in files:
        if filename.endswith((".jpg", ".png")):
            image = Image.open(os.path.join(input_directory, filename))
            resized_image = image.resize(target_size, Image.ANTIALIAS)
            output_path = os.path.join(output_directory, filename)
            resized_image.save(output_path)