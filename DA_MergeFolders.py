import arcpy
import os
# Enable overwriting
arcpy.env.overwriteOutput = True
input_folder = r"C:\acgis\project\source\DA_OwnersCoreInNeed"
output_file = r"C:\acgis\project\source\output\DA_OwnersCoreInNeed.shp"

shp_files = []

# Recursively search for shapefiles in the input folder and its subfolders
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".shp"):
            shp_files.append(os.path.join(root, file))

if len(shp_files) > 0:
    arcpy.management.Merge(shp_files, output_file)
    print("Merge completed successfully.")
else:
    print("No shapefiles found in the input folder.")



