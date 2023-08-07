import arcpy
import os

# Set the workspace environment
arcpy.env.workspace = r"C:\acgis\project\working\HousingCensus2021\HousingCensus2021.gdb"

# Define the target feature dataset
target_dataset = "DA_files"

# Define the existing value field name
value_field = "Value"

# Get a list of feature classes in the target dataset
feature_classes = arcpy.ListFeatureClasses(feature_dataset=target_dataset)

# Iterate over the feature classes
for feature_class in feature_classes:
    # Generate the field name based on the shapefile name
    field_name = os.path.splitext(feature_class)[0]
    
    # Check if the field already exists in the feature class
    field_names = [field.name for field in arcpy.ListFields(feature_class)]
    if field_name in field_names:
        print(f"Field {field_name} already exists in {feature_class}. Skipping...")
        continue

    # Add the field to the feature class
    arcpy.management.AddField(feature_class, field_name, "DOUBLE")

    # Calculate the new field to equal the existing value field
    arcpy.management.CalculateField(feature_class, field_name, "!" + value_field + "!", "PYTHON3")

print("Field addition and calculation completed.")
