from api.endpoints.cart_api import CartAPI
from api.validations.response_validator import ResponseValidator
from config.config import BASE_URL

cart_api = CartAPI(BASE_URL)


def test_add_to_cart():

    response = cart_api.add_valid_cart()

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


def test_invalid_cart():

    response = cart_api.add_invalid_cart()

    response_json = response.json()

    print(response.status_code)
    print(response_json)

    assert response.status_code in [201, 400, 404]