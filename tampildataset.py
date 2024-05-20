import os
import cv2
import matplotlib.pyplot as plt

def load_images_from_folder(folder):
    images = []
    if not os.path.exists(folder):
        print(f"Folder {folder} does not exist")
        return images
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        if os.path.isfile(img_path):  # Check if it is a file
            img = cv2.imread(img_path)
            if img is not None:
                images.append(img)
    return images

dataset_path = '/home/baldi/code/nia/dataset'
all_images = []
labels = []

# Iterate through each folder (1, 2, ..., 11)
for label in range(1, 12):
    folder_path = os.path.join(dataset_path, str(label))
    images = load_images_from_folder(folder_path)
    all_images.extend(images)
    labels.extend([label] * len(images))

# Check if we have images to display
if not all_images:
    print("No images found in the dataset.")
else:
    # Determine the grid size
    nrows = (len(all_images) + 4) // 5  # 5 images per row, calculate number of rows

    # Display images in a grid
    fig, axes = plt.subplots(nrows=nrows, ncols=5, figsize=(15, nrows * 3))
    for idx, (img, label) in enumerate(zip(all_images, labels)):
        row = idx // 5
        col = idx % 5
        ax = axes[row, col] if nrows > 1 else axes[col]  # Handle single row case
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.axis('off')
        ax.set_title(f'Label: {label}')

    # Hide any unused subplots
    for i in range(len(all_images), nrows * 5):
        row = i // 5
        col = i % 5
        if nrows > 1:
            axes[row, col].axis('off')
        else:
            axes[col].axis('off')

    plt.tight_layout()
    plt.show()
