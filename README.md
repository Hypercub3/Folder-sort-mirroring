# **Documentation: Folder Structure Mirroring Script**

## **Overview**
This script mirrors the folder structure of a source folder onto a destination folder, ensuring that files with the same base names (ignoring extensions) are placed in corresponding subdirectories.

---

## **Functionality**
- **Purpose**: To match files with the same name (regardless of extension) in a source and destination folder and move them into the appropriate subdirectories.
- **Key Features**:
  - Recursively traverses both source and destination folders.
  - Creates subdirectories in the destination folder to mirror the source folder.
  - Moves files with matching names into the corresponding subdirectory.

---

## **Script Details**
### **Dependencies**
- The script requires Python's built-in libraries:
  - `os` (for file system operations)
  - `shutil` (for file movement)

To run the script, no additional packages are required.

---

## **Code Explanation**

### **Function: `mirror_structure`**
```python
mirror_structure(source_folder, destination_folder)
```
- **Parameters**:
  - `source_folder`: The root folder whose structure and file names are mirrored.
  - `destination_folder`: The folder where files with matching names will be organized.

- **Behavior**:
  1. Ensures the destination folder exists.
  2. Iterates through all subdirectories and files in the `source_folder`.
  3. Extracts base names (i.e., file names without extensions).
  4. Searches for matching base names in the `destination_folder`.
  5. Moves the matching files into the corresponding subdirectories in the destination folder.

### **Sample Code Snippet**:
```python
for file_name in files:
    file_base_name, _ = os.path.splitext(file_name)

    for dest_root, _, dest_files in os.walk(destination_folder):
        for dest_file in dest_files:
            dest_base_name, _ = os.path.splitext(dest_file)

            if dest_base_name == file_base_name:
                src_file = os.path.join(dest_root, dest_file)
                dest_file_path = os.path.join(destination_path, dest_file)
                shutil.move(src_file, dest_file_path)
                print(f"Moved: {src_file} to {dest_file_path}")
```

### **Main Script Execution**:
```python
if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ").strip()
    destination_folder = input("Enter the destination folder path: ").strip()
    mirror_structure(source_folder, destination_folder)
```
- Takes user input for the source and destination folder paths.
- Calls the `mirror_structure` function.

---

## **Example Usage**
### **Folder Structure Before Execution**:

**Source Folder**:
```
source/
    subdir1/
        fileA.txt
    subdir2/
        fileB.doc
```

**Destination Folder**:
```
destination/
    fileA.jpg
    fileB.pdf
```

### **Folder Structure After Execution**:

**Destination Folder**:
```
destination/
    subdir1/
        fileA.jpg
    subdir2/
        fileB.pdf
```

---

## **Usage Instructions**
1. Save the script as `mirror_structure.py`.
2. Run the script in a terminal or command prompt.
3. Enter the full paths of the source and destination folders when prompted.

---

## **Considerations and Assumptions**
- The script matches files based on their base names (case-sensitive).
- If multiple files in the destination folder have the same base name, they will be moved according to the first match.
- The script moves the files; it does not copy them.
- Unmatched files in the destination folder remain untouched.

---

## **Potential Enhancements**
- Add logging for more detailed file operations.
- Allow case-insensitive matching.
- Add an option to copy files instead of moving them.
- Implement error handling for missing permissions or read-only files.

---

## **Conclusion**
This script simplifies the process of organizing files into a mirrored directory structure based on matching base names. It is ideal for situations where consistency in file organization across folders is needed.

## Full Code

```python

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

```

