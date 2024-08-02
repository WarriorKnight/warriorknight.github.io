import json

def sort_filenames(filenames):
    # Extract the numeric part and sort the filenames based on these numbers
    def extract_number(filename):
        # Extract number from filename format "X.json"
        return int(filename.split('.')[0])
    
    return sorted(filenames, key=extract_number)

def process_file(filepath):
    try:
        # Read the JSON content from the file
        with open(filepath, 'r') as file:
            filenames = json.load(file)
        
        # Sort the filenames
        sorted_filenames = sort_filenames(filenames)
        
        # Write the sorted filenames back to the file
        with open(filepath, 'w') as file:
            json.dump(sorted_filenames, file, indent=4)
        
        print(f"File '{filepath}' has been sorted and updated successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file '{filepath}' does not contain valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Path to the JSON file as a variable

file_path = '12/fileList.json'  # Change this to your file path

# Process the file
process_file(file_path)
