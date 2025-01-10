import os
import shutil

def mirror_structure(source_folder, destination_folder):
    # Ensure destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Walk through source folder
    for root, _, files in os.walk(source_folder):
        # Compute the relative path from the source folder
        relative_path = os.path.relpath(root, source_folder)
        destination_path = os.path.join(destination_folder, relative_path)

        # Ensure the relative path exists in the destination folder
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        # Process each file in the current source folder
        for file_name in files:
            file_base_name, _ = os.path.splitext(file_name)

            # Find a matching file in the destination folder
            for dest_root, _, dest_files in os.walk(destination_folder):
                for dest_file in dest_files:
                    dest_base_name, _ = os.path.splitext(dest_file)

                    # If the base names match, move the file to the correct subdirectory
                    if dest_base_name == file_base_name:
                        src_file = os.path.join(dest_root, dest_file)
                        dest_file_path = os.path.join(destination_path, dest_file)

                        # Move the file to the mirrored structure
                        shutil.move(src_file, dest_file_path)
                        print(f"Moved: {src_file} to {dest_file_path}")

if __name__ == "__main__":
    # Define source and destination folders
    source_folder = input("Enter the source folder path: ").strip()
    destination_folder = input("Enter the destination folder path: ").strip()

    # Call the function to mirror the structure
    mirror_structure(source_folder, destination_folder)
