import arcpy

# Set the workspace environment
arcpy.env.workspace = r"C:\acgis\project"

# Define the input DBF file and the feature class
CD_dbf = r"C:\acgis\project\source\output\CDHousing2021.dbf"
cd_fc = r"C:\acgis\project\source\CensusBoundary\CD.gdb\CD"

# Define the field names to join on
cd_dbf_join_field = "Geography"  # Field name in the DBF file
cd_feature_join_field = "DGUID"  # Field name in the feature class

# Perform the join
arcpy.JoinField_management(cd_fc, cd_feature_join_field, CD_dbf, cd_dbf_join_field)

# Output joined feature class
cd_output = r"C:\acgis\project\working\HousingCensus2021\HousingCensus2021.gdb\Working\CD_2021_Housing.shp"
arcpy.management.CopyFeatures(cd_fc, cd_output)
