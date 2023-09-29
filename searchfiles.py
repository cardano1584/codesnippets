import os

def search_files_in_folder(folder_path, substring):
    matching_files = []
    
    # Iterate over all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', errors='ignore') as f:  # errors='ignore' to handle potential encoding issues
                content = f.read()
                if substring in content:
                    matching_files.append(file_path)
    
    return matching_files

folder = "/path/to/folder"
substring = "your_substring"
result = search_files_in_folder(folder, substring)
print(result)
