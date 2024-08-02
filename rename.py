import os

def rename_files_in_directory(root_dir, prefix_to_remove):
    # Walk through all directories and files
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.startswith(prefix_to_remove):
                # Construct the new filename by removing the prefix
                new_filename = filename[len(prefix_to_remove):]
                # Construct full paths for old and new filenames
                old_file = os.path.join(dirpath, filename)
                new_file = os.path.join(dirpath, new_filename)
                
                # Rename the file
                try:
                    os.rename(old_file, new_file)
                    print(f"Renamed: {old_file} -> {new_file}")
                except Exception as e:
                    print(f"Error renaming file {old_file}: {e}")

if __name__ == "__main__":
    root_dir = "."  # Change this to the root directory you want to scan
    prefix_to_remove = "paragraph_"
    rename_files_in_directory(root_dir, prefix_to_remove)
