import os
import shutil
import random

# Set random seed for reproducibility
random.seed(42)

# Input and output directories
input_dir = "data"
output_base_dir = "split-data"
train_dir = os.path.join(output_base_dir, "train")
val_dir = os.path.join(output_base_dir, "val")
classes = ["female", "male"]

# Create necessary folders
for cls in classes:
    os.makedirs(os.path.join(train_dir, cls), exist_ok=True)
    os.makedirs(os.path.join(val_dir, cls), exist_ok=True)

# Process each class
for cls in classes:
    class_input_path = os.path.join(input_dir, cls)
    images = os.listdir(class_input_path)
    images = [img for img in images if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)

    # Split into 80% train, 20% val
    split_index = int(0.8 * len(images))
    train_images = images[:split_index]
    val_images = images[split_index:]

    # Copy train images
    for img in train_images:
        src = os.path.join(class_input_path, img)
        dst = os.path.join(train_dir, cls, img)
        shutil.copy2(src, dst)

    # Copy val images
    for img in val_images:
        src = os.path.join(class_input_path, img)
        dst = os.path.join(val_dir, cls, img)
        shutil.copy2(src, dst)

print("Done!")
