import os
import shutil

def organize_jpg_files(source_dir, target_dir):
    """Moves all .jpg files from the source directory to the target directory."""
    # Ensure target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created target directory: {target_dir}")

    try:
        # List all files in the source directory
        files = os.listdir(source_dir)
        moved_count = 0

        for file_name in files:
            # Check for .jpg extension (case-insensitive)
            if file_name.lower().endswith('.jpg'):
                source_path = os.path.join(source_dir, file_name)
                target_path = os.path.join(target_dir, file_name)
                
                # Move the file
                shutil.move(source_path, target_path)
                print(f"Moved: {file_name} -> {target_dir}")
                moved_count += 1

        print(f"\nTask complete! Successfully moved {moved_count} image(s).")

    except FileNotFoundError:
        print(f"Error: The directory '{source_dir}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define your paths here
    SOURCE = "./source_folder"
    TARGET = "./images_folder"
    
    # Create a dummy source folder for testing if it doesn't exist
    if not os.path.exists(SOURCE):
        os.makedirs(SOURCE)
        print(f"Created '{SOURCE}' for testing. Add some .jpg files here and rerun.")
    else:
        organize_jpg_files(SOURCE, TARGET)