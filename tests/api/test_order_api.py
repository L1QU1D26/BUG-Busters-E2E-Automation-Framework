from api.endpoints.order_api import OrderAPI
from api.validations.response_validator import ResponseValidator
from config.config import BASE_URL

order_api = OrderAPI(BASE_URL)


def test_create_order():

    response = order_api.create_valid_order()

    response_json = response.json()

    print(response.status_code)
    print(response_json)

    ResponseValidator.validate_status_code(
        response,
        201
    )

    ResponseValidator.validate_response_time(
        response,
        5
    )

    ResponseValidator.validate_key(
        response_json,
        "products"
    )

    assert response_json["products"][0]["id"] == 1


def test_order_with_missing_fields():

    response = order_api.create_invalid_order()

    response_json = response.json()

    print(response.status_code)
    print(response_json)

    assert response.status_code in [201, 400, 404]