import arcpy

# Set the workspace environment
arcpy.env.workspace = r"C:\acgis\project\working\HousingCensus2021\HousingCensus2021.gdb"

# Specify the input feature class
input_fc = "CD_Housing_2021"
# Define a dictionary with the field name and the new alias
field_alias_mapping = {
    "OBJECTID": None,
    "Shape": None,
    "CDUID": None,
    "DGUID": None,
    "CDNAME": "CD Name",
    "CDTYPE": "CD Type",
    "LANDAREA": "Land Area",
    "PRUID": None,
    "OID_1": None,
    "Geography": "DGUID",
    "TotalDwell": "Total - Dwelling condition",
    "RegMaintNe": "Regular maintenance needed",
    "MinRepNeed": "Minor repairs needed",
    "MajRepNeed": "Major repairs needed",
    "CoreNeed": "Total - In Core Need",
    "TotalExami": "Household examined for core housing need",
    "InCoreNeed": "In Core Need",
    "NotInCoreN": "Not in Core Need",
    "NA_x": "Core Housing Need Not Applicable",
    "Total": "Total - Tenure including presence of mortgage payments and subsidized housing",
    "Owner": None,
    "WithMortga": "With mortgage",
    "Wo_mortgag": "Without mortgage",
    "Renter": None,
    "Subsid_hou": "Subsidized housing",
    "NotSubsid": "Not subsidized housing",
    "DwellProvi": "Dwelling provided by the local government, First Nation, or Indian band",
    "Cost_incom": "Total - Shelter cost to income ratio",
    "F_30": "Spending less than 30 percent of income on shelter costs",
    "F_15": "Spending less than 15 percent of income on shelter costs",
    "F15_30": "Spending 15 percent to less than 30 percent of income on shelter costs",
    "F_30_1": "Spending 30 percent or more of income on shelter costs",
    "F30_50": "Spending 30 percent to less than 50 percent of income on shelter costs",
    "F_50": "Spending 50 percent or more of income on shelter costs",
    "F50_100": "Spending 50 percent to less than 100 percent of income on shelter costs",
    "NA_y": "Not Applicable - Shelter cost to income ratio",
    "TotHousiSu": "Total - Housing suitability",
    "Suitable": "Suitable housing",
    "NotSuitabl": "Not suitable housing",
    "Shape_Length": "Shape_Length",
    "Shape_Area": "Shape_Area"
}

# Iterate through the field_alias_mapping dictionary and update the field aliases
for field_name, new_alias in field_alias_mapping.items():
    if new_alias is not None:
        arcpy.AlterField_management(input_fc, field_name, new_field_alias=new_alias)

# Get a list of fields in the feature class
field_list = arcpy.ListFields(input_fc)

# Print the updated field aliases
for field in field_list:
    print(field.name, "-", field.aliasName)