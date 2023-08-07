import arcpy

# Set the workspace environment
arcpy.env.workspace = r"C:\acgis\project\working\HousingCensus2021\HousingCensus2021.gdb"

# Specify the input feature class
input_fc = "DisseminationAreas_21"
# Define a dictionary with the field name and the new alias
# Define the field aliases
field_aliases = {
    "DA_Household30PlusIncome": "Households spending 30 percent or more of income on shelter costs (%)",
    "DA_PercUnsuitable": "Households in unsuitable housing (%)",
    "DA_PercMajRepairs": "Households in dwellings in need of major repair (%)",
    "DA_EstValueDwell": "Average owner-estimated value of dwelling ($)",
    "DA_RenterAvgCost": "Average shelter cost for renter households ($)",
    "DA_Owner30PlusIncome": "Owner households spending 30 percent or more of income on shelter costs (%)",
    "DA_RentersCoreInNeed": "Renter households in core housing need (%)",
    "DA_Renter30PlusIncome": "Renter households spending 30 percent or more of income on shelter costs (%)",
    "DA_OwnersCoreInNeed": "Owner households in core housing need (%)"
}

# Update the field aliases
for field, alias in field_aliases.items():
    arcpy.AlterField_management(input_fc, field, new_field_alias=alias)

print("Field aliases updated successfully.")

# Get a list of fields in the feature class
field_list = arcpy.ListFields(input_fc)

# Print the updated field aliases
for field in field_list:
    print(field.name,":", field.aliasName)
    
