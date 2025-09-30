import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.calculate_post200_response import CalculatePost200Response  # noqa: E501
from openapi_server.models.calculate_post_request import CalculatePostRequest  # noqa: E501
from openapi_server.models.greets_get200_response import GreetsGet200Response  # noqa: E501
from openapi_server import util

from services.app_service import handle_greets, handle_calculate

def calculate_post(body):  # noqa: E501
    num1 = body.get('num1')
    num2 = body.get('num2')
    result = handle_calculate(num1, num2)
    return CalculatePost200Response(result=result)

def greets_get():  # noqa: E501
    message = handle_greets()
    return GreetsGet200Response(message=message)
