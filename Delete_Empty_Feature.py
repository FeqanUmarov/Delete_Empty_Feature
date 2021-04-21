import arcpy
from arcpy import env
input_database = arcpy.GetParameterAsText(0)
env.workspace = input_database
list_feature = arcpy.ListFeatureClasses("*")
for obj in list_feature:
    count = str(arcpy.GetCount_management(obj))
    if count == "0":
        arcp.Delete_management(obj)
