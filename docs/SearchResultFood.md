# SearchResultFood


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fdc_id** | **int** | Unique ID of the food. | 
**description** | **str** | The description of the food. | 
**data_type** | **str** | The type of the food data. | [optional] 
**food_code** | **str** | Any A unique ID identifying the food within FNDDS. | [optional] 
**food_nutrients** | [**[AbridgedFoodNutrient]**](AbridgedFoodNutrient.md) |  | [optional] 
**publication_date** | **str** | Date the item was published to FDC. | [optional] 
**scientific_name** | **str** | The scientific name of the food. | [optional] 
**brand_owner** | **str** | Brand owner for the food. Only applies to Branded Foods. | [optional] 
**gtin_upc** | **str** | GTIN or UPC code identifying the food. Only applies to Branded Foods. | [optional] 
**ingredients** | **str** | The list of ingredients (as it appears on the product label). Only applies to Branded Foods. | [optional] 
**ndb_number** | **str** | Unique number assigned for foundation foods. Only applies to Foundation and SRLegacy Foods. | [optional] 
**additional_descriptions** | **str** | Any additional descriptions of the food. | [optional] 
**all_highlight_fields** | **str** | allHighlightFields | [optional] 
**score** | **float** | Relative score indicating how well the food matches the search criteria. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


