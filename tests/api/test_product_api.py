import pytest
from api.endpoints.product_api import ProductAPI
from api.validations.response_validator import ResponseValidator
from config.config import BASE_URL

product_api = ProductAPI(BASE_URL)

@pytest.mark.xfail(reason="DummyJSON instability / HTTP 520 / timeouts on remote endpoints")
def test_get_all_products():

    response = product_api.get_all_products()

    response_json = response.json()

    print(response.status_code)
    print(response_json)

    ResponseValidator.validate_status_code(
        response,
        200
    )


@pytest.mark.xfail(reason="DummyJSON instability / HTTP 520 / timeouts on remote endpoints")
def test_get_single_product():

    response = product_api.get_single_product(1)

    response_json = response.json()

    print(response.status_code)
    print(response_json)

    ResponseValidator.validate_status_code(
        response,
        200
    )


@pytest.mark.xfail(reason="DummyJSON instability / HTTP 520 / timeouts on remote endpoints")
def test_invalid_product():

    response = product_api.get_single_product(
        999999
    )

    print(response.status_code)
    print(response.json())

    ResponseValidator.validate_status_code(
        response,
        404
    )