"""
    Food Data Central API

    The FoodData Central API provides REST access to FoodData Central (FDC). It is intended primarily to assist application developers wishing to incorporate nutrient data into their applications or websites.   To take full advantage of the API, developers should familiarize themselves with the database by reading the database documentation available via links on [Data Type Documentation](https://fdc.nal.usda.gov/data-documentation.html). This documentation provides the detailed definitions and descriptions needed to understand the data elements referenced in the API documentation.      Additional details about the API including rate limits, access, and licensing are available on the [FDC website](https://fdc.nal.usda.gov/api-guide.html)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.food_attribute import FoodAttribute
from openapi_client.model.food_portion import FoodPortion
from openapi_client.model.input_food_survey import InputFoodSurvey
from openapi_client.model.wweia_food_category import WweiaFoodCategory
globals()['FoodAttribute'] = FoodAttribute
globals()['FoodPortion'] = FoodPortion
globals()['InputFoodSurvey'] = InputFoodSurvey
globals()['WweiaFoodCategory'] = WweiaFoodCategory
from openapi_client.model.survey_food_item import SurveyFoodItem


class TestSurveyFoodItem(unittest.TestCase):
    """SurveyFoodItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSurveyFoodItem(self):
        """Test SurveyFoodItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SurveyFoodItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
