import arcpy

# Set the workspace environment
arcpy.env.workspace = r"C:\acgis\project\working\HousingCensus2021\HousingCensus2021.gdb"

# Specify the input feature class
input_fc = "CensusSubdivision_21"

# Get a list of fields in the feature class
field_list = arcpy.ListFields(input_fc)

# Print the updated field aliases
for field in field_list:
    print(f'{field.aliasName} (count), ')