import os
import cv2
import matplotlib.pyplot as plt

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

dataset_path = 'home/baldi/code/nia/dataset'
all_images = []
labels = []

# Iterate through each folder (1, 2, ..., 11)
for label in range(1, 12):
    folder_path = os.path.join(dataset_path, str(label))
    images = load_images_from_folder(folder_path)
    all_images.extend(images)
    labels.extend([label] * len(images))

# Display images in a grid
fig, axes = plt.subplots(nrows=8, ncols=5, figsize=(15, 15))
for idx, (img, label) in enumerate(zip(all_images, labels)):
    row = idx // 5
    col = idx % 5
    ax = axes[row, col]
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    ax.axis('off')
    ax.set_title(f'Label: {label}')

plt.tight_layout()
plt.show()
