# FoodsCriteria

JSON for request body of 'foods' POST request. Retrieves a list of food items by a list of up to 20 FDC IDs. Optional format and nutrients can be specified. Invalid FDC ID's or ones that are not found are omitted and an empty set is returned if there are no matches.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fdc_ids** | **[int]** | List of multiple FDC ID&#39;s | [optional] 
**format** | **str** | Optional. &#39;abridged&#39; for an abridged set of elements, &#39;full&#39; for all elements (default). | [optional] 
**nutrients** | **[int]** | Optional. List of up to 25 nutrient numbers. Only the nutrient information for the specified nutrients will be returned.  If a food does not have any matching nutrients, the food will be returned with an empty foodNutrients element. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


