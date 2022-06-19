"""
    BOAVIZTAPI - DEMO

    # 🎯 Retrieving the impacts of digital elements This is a quick demo, to see full documentation [click here](https://doc.api.boavizta.org)  ## ➡️Server router  ### Server routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |     X    | |   ADP  |        X       |     X    | |   PE   |        X       |     X    | ## ➡️Cloud router  ### Cloud routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |     X    | |   ADP  |        X       |     X    | |   PE   |        X       |     X    | ## ➡️Component router  ### Component routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |          | |   ADP  |        X       |          | |   PE   |        X       |          |   # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from boaviztapi_sdk.api_client import ApiClient, Endpoint as _Endpoint
from boaviztapi_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from boaviztapi_sdk.model.http_validation_error import HTTPValidationError
from boaviztapi_sdk.model.usage_cloud import UsageCloud


class CloudApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.instance_cloud_impact_v1_cloud_aws_post_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/v1/cloud/aws',
                'operation_id': 'instance_cloud_impact_v1_cloud_aws_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'instance_type',
                    'verbose',
                    'usage_cloud',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'instance_type':
                        (str,),
                    'verbose':
                        (bool,),
                    'usage_cloud':
                        (UsageCloud,),
                },
                'attribute_map': {
                    'instance_type': 'instance_type',
                    'verbose': 'verbose',
                },
                'location_map': {
                    'instance_type': 'query',
                    'verbose': 'query',
                    'usage_cloud': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.server_get_all_archetype_name_v1_cloud_aws_all_instances_get_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/v1/cloud/aws/all_instances',
                'operation_id': 'server_get_all_archetype_name_v1_cloud_aws_all_instances_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def instance_cloud_impact_v1_cloud_aws_post(
        self,
        **kwargs
    ):
        """Instance Cloud Impact  # noqa: E501

        # ✔️AWS instance impacts from instance type and usage  ### 📋 Instance type  AWS name of the chosen instance. You can retrieve the [list here](#/cloud/server_get_all_archetype_name_v1_cloud_all_aws_instances_get). ### 👄 Verbose If set at true, shows the impacts of each components and the value used for each attributes    ### ⏲ Duration Usage impacts are given for a specific time duration. Duration can be given : | time unit | Usage parameter | |------|-----| | HOURS | ```hours_use_time``` | | DAYS | ```days_use_time``` | | YEARS | ```years_use_time``` | *Note* : units are cumulative ### 🧮 Measure  🔨 Manufacture impacts are the sum of the pre-registered components impacts divided by the number of instances host in the physicall server  🔌 Usage impacts are measured by multiplying : * a **duration**  * an **impact factor** (```gwp_factor```, ```pe_factor```, ```adp_factor```) - retrieve with ```usage_location``` if not given  * The ```time``` per load in ```workload``` object. The ```power``` per load is retreive from the ```instance_type```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.instance_cloud_impact_v1_cloud_aws_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            instance_type (str): [optional]
            verbose (bool): [optional] if omitted the server will use the default value of True
            usage_cloud (UsageCloud): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.instance_cloud_impact_v1_cloud_aws_post_endpoint.call_with_http_info(**kwargs)

    def server_get_all_archetype_name_v1_cloud_aws_all_instances_get(
        self,
        **kwargs
    ):
        """Server Get All Archetype Name  # noqa: E501

        # ✔️Get all the available aws instances Return the name of all pre-registered aws instances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.server_get_all_archetype_name_v1_cloud_aws_all_instances_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.server_get_all_archetype_name_v1_cloud_aws_all_instances_get_endpoint.call_with_http_info(**kwargs)

