import os
import shutil

# Function to get a valid directory path from the user
def get_directory_input(prompt):
    while True:
        directory = input(prompt)
        if os.path.isdir(directory):
            return directory
        else:
            print(f"'{directory}' is not a valid directory. Please try again.")

# Define the file categories and their extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Scripts': ['.py', '.js', '.html', '.css', '.cpp'],
    'Archives': ['.zip', '.rar', '.tar.gz', '.7z'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv']
}

# Get the directory to organize from the user
source_dir = get_directory_input("Enter the path of the directory you want to organize: ")

# Create categorized folders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(source_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Iterate through files in the source directory
for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Move files to their respective categories
    file_extension = os.path.splitext(file_name)[1].lower()
    moved = False

    for folder, extensions in file_types.items():
        if file_extension in extensions:
            shutil.move(file_path, os.path.join(source_dir, folder, file_name))
            moved = True
            break

    # Handle files that don't match any category
    if not moved:
        misc_folder = os.path.join(source_dir, 'Miscellaneous')
        if not os.path.exists(misc_folder):
            os.makedirs(misc_folder)
        shutil.move(file_path, os.path.join(misc_folder, file_name))

print("File organization completed successfully!")
