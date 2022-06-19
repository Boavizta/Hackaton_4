"""
    BOAVIZTAPI - DEMO

    # 🎯 Retrieving the impacts of digital elements This is a quick demo, to see full documentation [click here](https://doc.api.boavizta.org)  ## ➡️Server router  ### Server routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |     X    | |   ADP  |        X       |     X    | |   PE   |        X       |     X    | ## ➡️Cloud router  ### Cloud routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |     X    | |   ADP  |        X       |     X    | |   PE   |        X       |     X    | ## ➡️Component router  ### Component routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |          | |   ADP  |        X       |          | |   PE   |        X       |          |   # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import boaviztapi_sdk
from boaviztapi_sdk.model.validation_error import ValidationError
globals()['ValidationError'] = ValidationError
from boaviztapi_sdk.model.http_validation_error import HTTPValidationError


class TestHTTPValidationError(unittest.TestCase):
    """HTTPValidationError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHTTPValidationError(self):
        """Test HTTPValidationError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HTTPValidationError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
