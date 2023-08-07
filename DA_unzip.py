import os
import zipfile

# Specify the folder path containing the zip files
folder_path = r"C:\acgis\project\source\DA_RentersCoreInNeed"
# Iterate through all files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    # Check if the file is a zip file
    if file_name.endswith(".zip"):
        # Create a unique folder name based on the file index
        folder_name = os.path.splitext(file_name)[0]
        folder_index = 1

        # Extract the contents of the zip file to the unique folder
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            while True:
                extract_folder = os.path.join(folder_path, f"{folder_name}_{folder_index}")
                if not os.path.exists(extract_folder):
                    break
                folder_index += 1

            zip_ref.extractall(extract_folder)

        print(f"Extracted: {file_name} to {extract_folder}")