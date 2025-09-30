import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.calculate_post200_response import CalculatePost200Response  # noqa: E501
from openapi_server.models.calculate_post_request import CalculatePostRequest  # noqa: E501
from openapi_server.models.greets_get200_response import GreetsGet200Response  # noqa: E501
from openapi_server import util


def calculate_post(body):  # noqa: E501
    """Performs a calculation

     # noqa: E501

    :param calculate_post_request: Input numbers for the calculation
    :type calculate_post_request: dict | bytes

    :rtype: Union[CalculatePost200Response, Tuple[CalculatePost200Response, int], Tuple[CalculatePost200Response, int, Dict[str, str]]
    """
    calculate_post_request = body
    if connexion.request.is_json:
        calculate_post_request = CalculatePostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def greets_get():  # noqa: E501
    """Returns a greeting message

     # noqa: E501


    :rtype: Union[GreetsGet200Response, Tuple[GreetsGet200Response, int], Tuple[GreetsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'
