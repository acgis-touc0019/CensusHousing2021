import arcpy
import os

# Set the workspace environment
arcpy.env.workspace = r"C:\acgis\project\source\output"
output_folder = r"C:\acgis\project\source\output"

# Iterate through each file in the folder
for file_name in os.listdir(arcpy.env.workspace):
    if file_name.endswith('.xlsx'):
        # Construct full file paths
        xlsx_file = os.path.join(arcpy.env.workspace, file_name)
        table_name = os.path.splitext(file_name)[0]

        # Create the output table path
        table_path = os.path.join(output_folder, f"{table_name}.dbf")

        # Convert XLSX to table
        arcpy.conversion.ExcelToTable(xlsx_file, table_path)
        print(f"Converted {xlsx_file} to {table_path}")