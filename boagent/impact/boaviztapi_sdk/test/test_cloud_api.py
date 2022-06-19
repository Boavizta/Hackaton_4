"""
    BOAVIZTAPI - DEMO

    # 🎯 Retrieving the impacts of digital elements This is a quick demo, to see full documentation [click here](https://doc.api.boavizta.org)  ## ➡️Server router  ### Server routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |     X    | |   ADP  |        X       |     X    | |   PE   |        X       |     X    | ## ➡️Cloud router  ### Cloud routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |     X    | |   ADP  |        X       |     X    | |   PE   |        X       |     X    | ## ➡️Component router  ### Component routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |          | |   ADP  |        X       |          | |   PE   |        X       |          |   # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import boaviztapi_sdk
from boaviztapi_sdk.api.cloud_api import CloudApi  # noqa: E501


class TestCloudApi(unittest.TestCase):
    """CloudApi unit test stubs"""

    def setUp(self):
        self.api = CloudApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_instance_cloud_impact_v1_cloud_aws_post(self):
        """Test case for instance_cloud_impact_v1_cloud_aws_post

        Instance Cloud Impact  # noqa: E501
        """
        pass

    def test_server_get_all_archetype_name_v1_cloud_aws_all_instances_get(self):
        """Test case for server_get_all_archetype_name_v1_cloud_aws_all_instances_get

        Server Get All Archetype Name  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
