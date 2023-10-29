import os
import shutil
import random

# Set the paths for your input (images and labels) and output (train, val, test) folders
input_images_dir = "images"
input_labels_dir = "labels"
output_dir = "final_data"  # This will contain train, val, and test folders

# Define the percentages for train, val, and test splits
train_ratio = 0.7  # 70% for training
val_ratio = 0.15  # 15% for validation
test_ratio = 0.15  # 15% for testing

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Create train, val, and test subdirectories within the output directory
train_dir = os.path.join(output_dir, "train")
val_dir = os.path.join(output_dir, "valid")
test_dir = os.path.join(output_dir, "test")

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

os.makedirs(os.path.join(train_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(train_dir, "labels"), exist_ok=True)
os.makedirs(os.path.join(val_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(val_dir, "labels"), exist_ok=True)
os.makedirs(os.path.join(test_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(test_dir, "labels"), exist_ok=True)

# Get a list of image and label files
image_files = os.listdir(input_images_dir)
label_files = os.listdir(input_labels_dir)

# Sort the lists to ensure they match
image_files.sort()
label_files.sort()

# Shuffle the indices for randomization
indices = list(range(len(image_files)))
random.shuffle(indices)

# Calculate the number of files for each split
# Calculate the number of files for each split
total_files = len(image_files)
train_split = int(total_files * train_ratio)
val_split = int(total_files * val_ratio)

# Copy the files to their respective directories
for i in range(total_files):
    src_image = os.path.join(input_images_dir, image_files[indices[i]])
    src_label = os.path.join(input_labels_dir, label_files[indices[i]])

    if i < train_split:
        dst_image = os.path.join(train_dir, "images", image_files[indices[i]])
        dst_label = os.path.join(train_dir, "labels", label_files[indices[i]])
    elif i < train_split + val_split:
        dst_image = os.path.join(val_dir, "images",image_files[indices[i]])
        dst_label = os.path.join(val_dir, "labels", label_files[indices[i]])
    else:
        dst_image = os.path.join(test_dir, "images",image_files[indices[i]])
        dst_label = os.path.join(test_dir, "labels", label_files[indices[i]])

    shutil.copy(src_image, dst_image)
    shutil.copy(src_label, dst_label)

print("Data splitting complete.")
