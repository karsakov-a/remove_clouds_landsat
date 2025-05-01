# -*- coding: utf-8 -*-
"""
Removes clouds and shadows based on the decrypted raster L8-9 QA_PIXEL Level-2.
Creates a layer of water content in the vector.
Fill the placeholders '##FILL THE PATH##'.
"""

import arcpy
from sys import argv


def L8911(Input_raster_QA_PIXEL_Landsat_8_9_L2=r"##FILL THE PATH##",
          Input_raster_to_apply_the_mask_extraction_to=r"##FILL THE PATH##",
          Path_to_save_raster_without_clouds=r"##FILL THE PATH##",
          Path_to_save_vector_layer_of_water=r"##FILL THE PATH##",
          Path_to_save_mask_of_clouds=r"##FILL THE PATH##"):

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True

    # Process: Raster to polygons (clouds) (conversion)
    with arcpy.EnvManager(outputMFlag="Disabled", outputZFlag="Disabled"):
        arcpy.conversion.RasterToPolygon(
            in_raster=Input_raster_QA_PIXEL_Landsat_8_9_L2,
            out_polygon_features=Path_to_save_vector_layer_of_water,
            simplify="NO_SIMPLIFY",
            raster_field="Value",
            create_multipart_features="MULTIPLE_OUTER_PART",
            max_vertices_per_feature=None)

    # Process: Select in the layer by attribute (clouds) (management)
    Selection_clouds_, Quantity_clouds_ = arcpy.management.SelectLayerByAttribute(
        in_layer_or_view=Path_to_save_vector_layer_of_water,
        selection_type="NEW_SELECTION",
        where_clause=("gridcode IN (56598, 21762, 21890, 22018, 22080, 22146, "
                      "22208, 22280, 23826, 23888, 24082, 24144, "
                      "29986, 54534, 54790, 54852, 55052, 56660,	"
                      "56854, 56916, 30242)"),
        invert_where_clause="INVERT")

    # Process: Extract by mask (sa)
    Extract_by_mask = Path_to_save_raster_without_clouds
    Path_to_save_raster_without_clouds = arcpy.sa.ExtractByMask(
        in_raster=Input_raster_to_apply_the_mask_extraction_to,
        in_mask_data=Selection_clouds_,
        extraction_area="INSIDE",

        ## FILL the coordinate system ##
        analysis_extent=(
            "331785 5762085 571815 6004815 PROJCS[\"WGS_1984_UTM_Zone_46N\","
            "GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\","
            "6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\","
            "0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],"
            "PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],"
            "PARAMETER[\"Central_Meridian\",93.0],PARAMETER[\"Scale_Factor\",0.9996],"
            "PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]"))
    Path_to_save_raster_without_clouds.save(Extract_by_mask)

    # Process: Select in the layer by attribute (water) (management)
    Selection_water_, Quantity_water_ = arcpy.management.SelectLayerByAttribute(
        in_layer_or_view=Path_to_save_vector_layer_of_water,
        selection_type="NEW_SELECTION",
        where_clause="gridcode IN (21952)",
        invert_where_clause="INVERT")

    # Process: Delete objects exclude water (management)
    Updated_input_data_with_deleted_objects = arcpy.management.DeleteRows(
        in_rows=Selection_water_)[0]

    # Process: Raster to polygons (mask of clouds) (conversion)
    Output_polygonal_objects = r"##FILL THE PATH##"
    with arcpy.EnvManager(outputMFlag="Disabled", outputZFlag="Disabled"):
        arcpy.conversion.RasterToPolygon(
            in_raster=Input_raster_QA_PIXEL_Landsat_8_9_L2,
            out_polygon_features=Output_polygonal_objects,
            simplify="NO_SIMPLIFY",
            raster_field="Value",
            create_multipart_features="MULTIPLE_OUTER_PART",
            max_vertices_per_feature=None)

    # Process: Select in the layer by attribute (mask of clouds) (management)
    Selection_mask_of_clouds_, Quantity_mask_of_clouds_ = arcpy.management.SelectLayerByAttribute(
        in_layer_or_view=Output_polygonal_objects,
        selection_type="NEW_SELECTION",
        where_clause="gridcode IN (56598, 21762, 21890, 22018, 22080, 22146, "
                     "22208, 22280, 23826, 23888, 24082, 24144, 29986, "
                     "54534, 54790,	54852, 55052, 56660, 56854, 56916,	30242)",
        invert_where_clause="NON_INVERT")

    # Process: Export objects (mask of clouds) (conversion)
    arcpy.conversion.ExportFeatures(
        in_features=Selection_mask_of_clouds_,
        out_features=Path_to_save_mask_of_clouds,
        where_clause="",
        use_field_alias_as_name="NOT_USE_ALIAS",
        field_mapping=(
            "Shape_Length \"Shape_Length\" false true true 0 Double 0 0,First,#,RasterT_LC08_L21_Layer,Shape_Length,"
            "-1,-1;Shape_Area \"Shape_Area\" false true true 0 Double 0 0,First,#,RasterT_LC08_L21_Layer,Shape_Area,"
            "-1,-1;ID \"ID\" true true false 0 Long 0 0,First,#,RasterT_LC08_L21_Layer,ID,-1,-1;"
            "GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0,First,#,RasterT_LC08_L21_Layer,GRIDCODE,-1,-1"),
        sort_field=[])


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"##FILL THE PATH##", workspace=r"##FILL THE PATH##"):
        L8911(*argv[1:])
