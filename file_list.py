import os
import json

def list_files_to_json(directory):
    # List all files in the specified directory
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
        return
    except PermissionError:
        print(f"Permission denied to access the directory {directory}.")
        return

    # Define the path for the output JSON file
    output_file = os.path.join(directory, "fileList.json")

    # Write the list of filenames to a JSON file
    try:
        with open(output_file, 'w') as json_file:
            json.dump(files, json_file, indent=4)
        print(f"File list has been written to {output_file}.")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

if __name__ == "__main__":
    for i in range (13):
        directory = str(i)  # Change this to the directory you want to scan
        list_files_to_json(directory)
