import unittest

from flask import json

from openapi_server.models.calculate_post200_response import CalculatePost200Response  # noqa: E501
from openapi_server.models.calculate_post_request import CalculatePostRequest  # noqa: E501
from openapi_server.models.greets_get200_response import GreetsGet200Response  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_calculate_post(self):
        """Test case for calculate_post

        Performs a calculation
        """
        calculate_post_request = openapi_server.CalculatePostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/calculate',
            method='POST',
            headers=headers,
            data=json.dumps(calculate_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_greets_get(self):
        """Test case for greets_get

        Returns a greeting message
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/greets',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
