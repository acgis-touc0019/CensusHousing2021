import pandas as pd
import os

# Specify the folder path where the XLSX files are located
folder_path = r"C:\acgis\project\source\Tables\DA"

# Get a list of all XLSX files in the folder
xlsx_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

# Create an empty DataFrame to store the joined result
joined_dataframe = None

# Iterate through the XLSX files and join them
for xlsx_file in xlsx_files:
    xlsx_path = os.path.join(folder_path, xlsx_file)
    xlsx_data = pd.read_excel(xlsx_path)
    
    if joined_dataframe is None:
        joined_dataframe = xlsx_data
    else:
        joined_dataframe = joined_dataframe.merge(xlsx_data, on='Geography', how='inner')

# Work with the joined DataFrame as needed
print(joined_dataframe)

# Specify the output XLSX file path
output_xlsx_file = r"C:\acgis\project\source\output\DAHousing.xlsx"

# Export the joined DataFrame to XLSX
joined_dataframe.to_excel(output_xlsx_file, index=False)
