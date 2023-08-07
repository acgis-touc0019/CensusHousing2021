import arcpy 
arcpy.env.workspace = r"C:\acgis\project\working\HousingCensus2021\HousingCensus2021.gdb"

import arcpy

# Specify the feature class path
feature_class = "DisseminationAreas_21"

# Specify the field names
field_names = ['DA_OwnPerc', 'DA_OwnerAvgCost', 'DA_Household30PlusIncome', 'DA_PercUnsuitable',
               'DA_PercMajRepairs', 'DA_EstValueDwell', 'DA_RenterAvgCost', 'DA_Owner30PlusIncome',
               'DA_RentersCoreInNeed', 'DA_Renter30PlusIncome', 'DA_OwnersCoreInNeed']

# Start an update cursor to iterate through the rows
with arcpy.da.UpdateCursor(feature_class, field_names) as cursor:
    for row in cursor:
        for i, field_value in enumerate(row):
            if not isinstance(field_value, (int, float)):
                row[i] = None  # Assign None to non-numeric values
        cursor.updateRow(row)

print("Non-numeric values assigned None for the specified fields.")
