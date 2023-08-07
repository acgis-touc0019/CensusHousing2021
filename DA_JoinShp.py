import arcpy
import os

arcpy.env.overwriteOutput = True

# Set the workspace environment
arcpy.env.workspace = r"C:\acgis\project\working\HousingCensus2021\HousingCensus2021.gdb"

# Define the target feature dataset and output feature class name
target_dataset = "DA_files"
output_dataset = "Working"
output_fc_name = "DA_Housing_MajorCities"
source_fc = "DA_OwnPerc"

# Create a FieldMappings object
field_mappings = arcpy.FieldMappings()

# Add the source field to the field mappings
field_mappings.addTable(source_fc)

# Find the index of the source field
source_field_index = field_mappings.findFieldMapIndex("DGUID")

# Get the field map object for the source field
field_map = field_mappings.getFieldMap(source_field_index)

# Set the output field name for the target feature class
field_map.outputField.name = "DGUID"

# Add the modified field map to the field mappings
field_mappings.replaceFieldMap(source_field_index, field_map)

# Copy the source feature class to the target feature class
arcpy.FeatureClassToFeatureClass_conversion(source_fc, output_dataset,output_fc_name, field_mapping=field_mappings)

print("Field copied successfully.")


# Fields to skip while adding to the output feature class
skip_fields = ["OBJECTID", "ESRI_OID", "Location", "Value", "Shape_Length", "Shape_Area", "DGUID_PK"]

# Get a list of feature classes in the target dataset
feature_classes = arcpy.ListFeatureClasses(feature_dataset=target_dataset)

# Check if there are feature classes in the target dataset
if feature_classes:
    # Create the output feature dataset if it does not exist
    if not arcpy.Exists(os.path.join(arcpy.env.workspace, output_dataset)):
        arcpy.management.CreateFeatureDataset(arcpy.env.workspace, output_dataset)
    
    
    # Generate the output feature class path
    output_fc = os.path.join(arcpy.env.workspace, output_dataset, output_fc_name)

    # Get the field names of the output feature class
    output_fields = [field.name for field in arcpy.ListFields(output_fc) if field.name not in skip_fields]

    # Iterate through the feature classes
    for fc in feature_classes:
        # Get the field names of the current feature class, excluding the skip_fields
        fc_fields = [field.name for field in arcpy.ListFields(fc) if field.name not in skip_fields]

        # Print the field names for debugging
        print(f"Field names for {fc}:")
        print(fc_fields)

        try:
            # Perform the join operation using the common field "DGUID"
            arcpy.management.JoinField(output_fc, "DGUID", fc, "DGUID", fc_fields)

        except Exception as e:
            print(f"Error joining {fc}: {str(e)}")
            continue

    print("Join operation completed.")
else:
    print("There are no feature classes in the target dataset.")
