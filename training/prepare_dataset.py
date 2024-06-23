import os
import shutil
import pandas as pd

def split_and_organize_dataset(root_dir, destination_dir):
    # Define paths
    train_images_dir = os.path.join(root_dir, 'train')
    test_images_dir = os.path.join(root_dir, 'test')
    train_metadata_path = os.path.join(root_dir, 'train.csv')
    test_metadata_path = os.path.join(root_dir, 'test.csv')
    
    # Define destination paths
    dest_train_dir = os.path.join(destination_dir, 'train')
    dest_val_dir = os.path.join(destination_dir, 'val')
    dest_test_dir = os.path.join(destination_dir, 'test')

    # Create destination directories
    os.makedirs(dest_train_dir, exist_ok=True)
    os.makedirs(dest_val_dir, exist_ok=True)
    os.makedirs(dest_test_dir, exist_ok=True)

    # Read metadata
    train_metadata = pd.read_csv(train_metadata_path)
    test_metadata = pd.read_csv(test_metadata_path)

    # Function to create label folders and move files
    def move_files(metadata, src_dir, base_dest_dir):
        for label in metadata['category'].unique():
            label_dir = os.path.join(base_dest_dir, label)
            os.makedirs(label_dir, exist_ok=True)
        
        for _, row in metadata.iterrows():
            src_path = os.path.join(src_dir, row['filename'])
            dst_path = os.path.join(base_dest_dir, row['category'], row['filename'])
            if os.path.exists(src_path):  # Ensure the source file exists before moving
                shutil.move(src_path, dst_path)

    # Split train data into train and val sets
    val_metadata = pd.DataFrame(columns=train_metadata.columns)
    updated_train_metadata = pd.DataFrame(columns=train_metadata.columns)

    for label in train_metadata['category'].unique():
        label_data = train_metadata[train_metadata['category'] == label]
        val_samples = label_data.sample(n=50, random_state=42)  # Change the random_state for reproducibility
        train_samples = label_data.drop(val_samples.index)
        
        val_metadata = pd.concat([val_metadata, val_samples])
        updated_train_metadata = pd.concat([updated_train_metadata, train_samples])

    # Move files to their respective folders
    move_files(updated_train_metadata, train_images_dir, dest_train_dir)
    move_files(val_metadata, train_images_dir, dest_val_dir)
    move_files(test_metadata, test_images_dir, dest_test_dir)

    print("Dataset split and organized into label-specific folders.")

# Example usage
root_dir = 'raw_data'  # Replace with your root directory path
destination_dir = 'data'  # Replace with your destination directory path
split_and_organize_dataset(root_dir, destination_dir)
