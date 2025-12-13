import os

DATASET_PATH = "dataset"
classes = os.listdir(DATASET_PATH)

print("Class distribution:")
for cls in classes:
    count = len(os.listdir(os.path.join(DATASET_PATH, cls)))
    print(f"{cls}: {count} images")
