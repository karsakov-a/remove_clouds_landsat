# Cloud Removal and Water Body Detection on Landsat 8–9 Satellite Imagery  
**Automated satellite data processing using the `arcpy` library**  

## **Description**  
This script is designed to process Landsat 8/9 Collection 2 Level 2 (L2) data to:  
1. Remove clouds and cloud shadows from raster data.  
2. Identify water bodies (e.g., rivers, lakes) using QA information (`QA_PIXEL`).  
3. Save results in raster and vector formats.  

Works with data obtained via the Landsat Collection 2 (L2SP) service.  

## **Documentation**  
[Landsat 8–9 Collection 2 Level 2 Product Guide]
(https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/LSDS-1619_Landsat8-9-Collection2-Level2-Science-Product-Guide-v6.pdf)  


## **Requirements**  
1. **ArcGIS Pro or ArcMap** (version 10.8 or later).  
   - `arcpy` module and **Spatial Analyst** extension.  
   - License for geoprocessing tools.  
2. **Python 3.9** (built-in with ArcGIS).  
3. No additional dependencies or libraries required.  

**Environment path**:  
`C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3`  

---

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
https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/LSDS-1619_Landsat8-9-Collection2-Level2-Science-Product-Guide-v6.pdf


## **Требования**  
1. **ArcGIS Pro или ArcMap** (версия 10.8 и выше).  
   - Модуль `arcpy` и расширение **Spatial Analyst**.  
   - Лицензия на использование геообработки.  
2. **Python 3.9** (встроенный в ArcGIS). 
3. Иные зависимости и библиотеки не используются.

Среда размещена по адресу C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3 

## **Контакт**
Teltgram @crashkkm