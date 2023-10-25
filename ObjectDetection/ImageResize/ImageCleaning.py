import os
import pyheif
from PIL import Image
from pillow_heif import register_heif_opener

# Directory containing your images
input_directory = "RawImages/"

# Directory to save the resized images
output_directory = "ResizedImages/"

# Target size

def heic_to_png(heic_path, png_path):
    try:
        # Open the HEIC image
        heif_file = pyheif.read(heic_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )

        # Save the image as PNG
        image.save(png_path, format="PNG")

        print(f'Conversion from {heic_path} to {png_path} completed successfully.')
    except Exception as e:
        print(f'Error: {e}')


# List all files in the input directory
files = os.listdir(input_directory)
if __name__ == "__main__":
    for filename in files:
        if filename.endswith((".jpg", ".png", ".heic")):
            file = os.path.splitext(filename)[0] + ".png"
            # image = Image.open(os.path.join(input_directory, filename))
            # resized_image = image.resize(target_size, Image.ANTIALIAS)
            output_path = os.path.join(output_directory, filename)
            # resized_image.save(output_path)
            heic_to_png(os.path.join(input_directory, filename), os.path.join(output_directory, file))