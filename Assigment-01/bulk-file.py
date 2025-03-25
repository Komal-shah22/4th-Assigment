import os

def bulk_rename(folder_path, prefix="file_", start_number=1):
    """
    Renames all files in the given folder with a new pattern.
    
    :param folder_path: Path to the folder where files are located.
    :param prefix: New name prefix (default: "file_").
    :param start_number: Starting number for renaming (default: 1).
    """
    if not os.path.exists(folder_path):
        print("❌ Error: Folder does not exist!")
        return

    files = os.listdir(folder_path)
    files.sort()  # Sort files alphabetically
    renamed_files = 0  # Counter to track renamed files

    for index, file_name in enumerate(files, start=start_number):
        old_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(old_path):  # Ensure it's a file, not a folder
            extension = os.path.splitext(file_name)[1]  # Get file extension
            new_name = f"{prefix}{index}{extension}"
            new_path = os.path.join(folder_path, new_name)
            
            os.rename(old_path, new_path)
            print(f" Renamed: {file_name} → {new_name}")
            renamed_files += 1

    # Show completion message only if files were renamed
    if renamed_files > 0:
        print("\n\t\t====== Renaming complete! Check your folder for the updated file names. =====")
    else:
        print("\n No files were renamed. Make sure there are valid files in the folder.")

# Welcome Message
print("\n\t\t\t========= Welcome to the Bulk File Renamer! ==========\n")
print("Easily rename multiple files in a folder with just one click!\n")

# Get folder path from user
folder = input(" Enter the full path of the folder: ").strip()
prefix = input(" Enter the new file name prefix (default: file_): ").strip() or "file_"

# Validate that the starting number is a valid integer
while True:
    start_num = input(" Enter the starting number (default: 1): ").strip()
    if start_num.isdigit():  # Check if input is a valid number
        start_num = int(start_num)
        break
    else:
        print("❌ Invalid input! Please enter a **number**, not letters.")

# Run the renaming function
bulk_rename(folder, prefix, start_num)
