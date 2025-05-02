# Cloud Removal and Water Body Detection on Landsat 8–9 Satellite Imagery  
**Automated satellite data processing using the `arcpy` library**  

## **Description**  
This script is designed to process Landsat 8/9 Collection 2 Level 2 (L2) data to:  
1. Remove clouds and cloud shadows from raster data.  
2. Identify water bodies (e.g., rivers, lakes) using QA information (`QA_PIXEL`).  
3. Save results in raster and vector formats.  

Works with data obtained via the Landsat Collection 2 (L2SP) service.  

## **Documentation**  
- [Landsat 8–9 Collection 2 Level 2 Product Guide](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/LSDS-1619_Landsat8-9-Collection2-Level2-Science-Product-Guide-v6.pdf)

- [Raster to Polygon (Conversion)](https://pro.arcgis.com/en/pro-app/3.0/tool-reference/conversion/raster-to-polygon.htm)
- [Select Layer By Attribute (Data Management)](https://pro.arcgis.com/en/pro-app/3.0/tool-reference/data-management/select-layer-by-attribute.htm)
- [Delete Rows (Data Management)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/delete-rows.htm)
- [Extract by Mask (Spatial Analyst)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/extract-by-mask.htm)
- [Export Features (Conversion)](https://pro.arcgis.com/en/pro-app/3.0/tool-reference/conversion/export-features.htm)
- [Run a model in ModelBuilder](https://pro.arcgis.com/en/pro-app/latest/help/analysis/geoprocessing/modelbuilder/run-a-model.htm)

## **Requirements**  
1. **ArcGIS Pro or ArcMap** (version 10.8 or later).  
   - `arcpy` module and **Spatial Analyst** extension.  
   - License for geoprocessing tools.  
2. **Python 3.9** (built-in with ArcGIS).
3. The Cloud Removal and Water Decryption by Landsat 8-9.atbx model is based on ArcGIS Pro 3.0.1
4. Model Builder version 3.0.1.36056
5. No additional dependencies or libraries required.  

**Environment path**:  
`C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3`  

## **Contact**  
Telegram: @crashkkm

---

# Удаление облаков и дешифрирование воды на спутниковых снимках Landsat 8–9 
**Автоматизированная обработка спутниковых данных с использованием библиотеки arcpy**

## **Описание**  
Этот скрипт предназначен для обработки данных Landsat 8/9 (L2) с целью:  
1. Удаления облаков и облачных теней из растровых данных.  
2. Выделения водных объектов (например, рек, озёр) на основе QA-информации (QA_PIXEL).  
3. Сохранения результатов в формате растра и векторного слоя.  

Работает с данными, полученными через сервис Landsat Collection 2 (L2SP).  

## **Документация**
- [Landsat 8–9 Collection 2 Level 2 Product Guide](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/LSDS-1619_Landsat8-9-Collection2-Level2-Science-Product-Guide-v6.pdf)

- [Растр в полигоны (Конвертация)](https://pro.arcgis.com/ru/pro-app/3.0/tool-reference/conversion/raster-to-polygon.htm)
- [Select Layer By Attribute (Data Management)](https://pro.arcgis.com/ru/pro-app/3.0/tool-reference/data-management/select-layer-by-attribute.htm)
- [Удалить строки (Управление данными)](https://pro.arcgis.com/ru/pro-app/latest/tool-reference/data-management/delete-rows.htm)
- [Извлечь по маске (Spatial Analyst)](https://pro.arcgis.com/ru/pro-app/latest/tool-reference/spatial-analyst/extract-by-mask.htm)
- [Экспорт объектов (Конвертация)](https://pro.arcgis.com/ru/pro-app/3.0/tool-reference/conversion/export-features.htm)
- [Запуск модели в ModelBuilder](https://pro.arcgis.com/ru/pro-app/latest/help/analysis/geoprocessing/modelbuilder/run-a-model.htm)


## **Требования**  
1. **ArcGIS Pro или ArcMap** (версия 10.8 и выше).  
   - Модуль `arcpy` и расширение **Spatial Analyst**.  
   - Лицензия на использование геообработки.  
2. **Python 3.9** (встроенный в ArcGIS).
3. Модель Cloud Removal and Water Decryption by Landsat 8-9.atbx сделана на базе ArcGIS Pro 3.0.1
4. Версия Model Builder 3.0.1.36056
5. Иные зависимости и библиотеки не используются.

Среда размещена по адресу C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3 

## **Контакт**
Telegram @crashkkm