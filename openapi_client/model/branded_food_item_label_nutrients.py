"""
    Food Data Central API

    The FoodData Central API provides REST access to FoodData Central (FDC). It is intended primarily to assist application developers wishing to incorporate nutrient data into their applications or websites.   To take full advantage of the API, developers should familiarize themselves with the database by reading the database documentation available via links on [Data Type Documentation](https://fdc.nal.usda.gov/data-documentation.html). This documentation provides the detailed definitions and descriptions needed to understand the data elements referenced in the API documentation.      Additional details about the API including rate limits, access, and licensing are available on the [FDC website](https://fdc.nal.usda.gov/api-guide.html)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_client.model.branded_food_item_label_nutrients_calcium import BrandedFoodItemLabelNutrientsCalcium
    from openapi_client.model.branded_food_item_label_nutrients_calories import BrandedFoodItemLabelNutrientsCalories
    from openapi_client.model.branded_food_item_label_nutrients_carbohydrates import BrandedFoodItemLabelNutrientsCarbohydrates
    from openapi_client.model.branded_food_item_label_nutrients_fat import BrandedFoodItemLabelNutrientsFat
    from openapi_client.model.branded_food_item_label_nutrients_fiber import BrandedFoodItemLabelNutrientsFiber
    from openapi_client.model.branded_food_item_label_nutrients_iron import BrandedFoodItemLabelNutrientsIron
    from openapi_client.model.branded_food_item_label_nutrients_postassium import BrandedFoodItemLabelNutrientsPostassium
    from openapi_client.model.branded_food_item_label_nutrients_protein import BrandedFoodItemLabelNutrientsProtein
    from openapi_client.model.branded_food_item_label_nutrients_saturated_fat import BrandedFoodItemLabelNutrientsSaturatedFat
    from openapi_client.model.branded_food_item_label_nutrients_sugars import BrandedFoodItemLabelNutrientsSugars
    from openapi_client.model.branded_food_item_label_nutrients_trans_fat import BrandedFoodItemLabelNutrientsTransFat
    globals()['BrandedFoodItemLabelNutrientsCalcium'] = BrandedFoodItemLabelNutrientsCalcium
    globals()['BrandedFoodItemLabelNutrientsCalories'] = BrandedFoodItemLabelNutrientsCalories
    globals()['BrandedFoodItemLabelNutrientsCarbohydrates'] = BrandedFoodItemLabelNutrientsCarbohydrates
    globals()['BrandedFoodItemLabelNutrientsFat'] = BrandedFoodItemLabelNutrientsFat
    globals()['BrandedFoodItemLabelNutrientsFiber'] = BrandedFoodItemLabelNutrientsFiber
    globals()['BrandedFoodItemLabelNutrientsIron'] = BrandedFoodItemLabelNutrientsIron
    globals()['BrandedFoodItemLabelNutrientsPostassium'] = BrandedFoodItemLabelNutrientsPostassium
    globals()['BrandedFoodItemLabelNutrientsProtein'] = BrandedFoodItemLabelNutrientsProtein
    globals()['BrandedFoodItemLabelNutrientsSaturatedFat'] = BrandedFoodItemLabelNutrientsSaturatedFat
    globals()['BrandedFoodItemLabelNutrientsSugars'] = BrandedFoodItemLabelNutrientsSugars
    globals()['BrandedFoodItemLabelNutrientsTransFat'] = BrandedFoodItemLabelNutrientsTransFat


class BrandedFoodItemLabelNutrients(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'fat': (BrandedFoodItemLabelNutrientsFat,),  # noqa: E501
            'saturated_fat': (BrandedFoodItemLabelNutrientsSaturatedFat,),  # noqa: E501
            'trans_fat': (BrandedFoodItemLabelNutrientsTransFat,),  # noqa: E501
            'cholesterol': (BrandedFoodItemLabelNutrientsTransFat,),  # noqa: E501
            'sodium': (BrandedFoodItemLabelNutrientsTransFat,),  # noqa: E501
            'carbohydrates': (BrandedFoodItemLabelNutrientsCarbohydrates,),  # noqa: E501
            'fiber': (BrandedFoodItemLabelNutrientsFiber,),  # noqa: E501
            'sugars': (BrandedFoodItemLabelNutrientsSugars,),  # noqa: E501
            'protein': (BrandedFoodItemLabelNutrientsProtein,),  # noqa: E501
            'calcium': (BrandedFoodItemLabelNutrientsCalcium,),  # noqa: E501
            'iron': (BrandedFoodItemLabelNutrientsIron,),  # noqa: E501
            'postassium': (BrandedFoodItemLabelNutrientsPostassium,),  # noqa: E501
            'calories': (BrandedFoodItemLabelNutrientsCalories,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'fat': 'fat',  # noqa: E501
        'saturated_fat': 'saturatedFat',  # noqa: E501
        'trans_fat': 'transFat',  # noqa: E501
        'cholesterol': 'cholesterol',  # noqa: E501
        'sodium': 'sodium',  # noqa: E501
        'carbohydrates': 'carbohydrates',  # noqa: E501
        'fiber': 'fiber',  # noqa: E501
        'sugars': 'sugars',  # noqa: E501
        'protein': 'protein',  # noqa: E501
        'calcium': 'calcium',  # noqa: E501
        'iron': 'iron',  # noqa: E501
        'postassium': 'postassium',  # noqa: E501
        'calories': 'calories',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """BrandedFoodItemLabelNutrients - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            fat (BrandedFoodItemLabelNutrientsFat): [optional]  # noqa: E501
            saturated_fat (BrandedFoodItemLabelNutrientsSaturatedFat): [optional]  # noqa: E501
            trans_fat (BrandedFoodItemLabelNutrientsTransFat): [optional]  # noqa: E501
            cholesterol (BrandedFoodItemLabelNutrientsTransFat): [optional]  # noqa: E501
            sodium (BrandedFoodItemLabelNutrientsTransFat): [optional]  # noqa: E501
            carbohydrates (BrandedFoodItemLabelNutrientsCarbohydrates): [optional]  # noqa: E501
            fiber (BrandedFoodItemLabelNutrientsFiber): [optional]  # noqa: E501
            sugars (BrandedFoodItemLabelNutrientsSugars): [optional]  # noqa: E501
            protein (BrandedFoodItemLabelNutrientsProtein): [optional]  # noqa: E501
            calcium (BrandedFoodItemLabelNutrientsCalcium): [optional]  # noqa: E501
            iron (BrandedFoodItemLabelNutrientsIron): [optional]  # noqa: E501
            postassium (BrandedFoodItemLabelNutrientsPostassium): [optional]  # noqa: E501
            calories (BrandedFoodItemLabelNutrientsCalories): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """BrandedFoodItemLabelNutrients - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            fat (BrandedFoodItemLabelNutrientsFat): [optional]  # noqa: E501
            saturated_fat (BrandedFoodItemLabelNutrientsSaturatedFat): [optional]  # noqa: E501
            trans_fat (BrandedFoodItemLabelNutrientsTransFat): [optional]  # noqa: E501
            cholesterol (BrandedFoodItemLabelNutrientsTransFat): [optional]  # noqa: E501
            sodium (BrandedFoodItemLabelNutrientsTransFat): [optional]  # noqa: E501
            carbohydrates (BrandedFoodItemLabelNutrientsCarbohydrates): [optional]  # noqa: E501
            fiber (BrandedFoodItemLabelNutrientsFiber): [optional]  # noqa: E501
            sugars (BrandedFoodItemLabelNutrientsSugars): [optional]  # noqa: E501
            protein (BrandedFoodItemLabelNutrientsProtein): [optional]  # noqa: E501
            calcium (BrandedFoodItemLabelNutrientsCalcium): [optional]  # noqa: E501
            iron (BrandedFoodItemLabelNutrientsIron): [optional]  # noqa: E501
            postassium (BrandedFoodItemLabelNutrientsPostassium): [optional]  # noqa: E501
            calories (BrandedFoodItemLabelNutrientsCalories): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
