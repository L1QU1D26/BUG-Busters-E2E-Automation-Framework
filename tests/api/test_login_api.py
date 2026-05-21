import pytest
from api.endpoints.auth_api import AuthAPI
from api.validations.response_validator import ResponseValidator
from config.config import BASE_URL

auth_api = AuthAPI(BASE_URL)


@pytest.mark.xfail(reason="DummyJSON instability / HTTP 520 / timeouts on auth endpoints")
def test_valid_login():

    response = auth_api.valid_login()

    response_json = response.json()

    print(response.status_code)
    print(response_json)

    ResponseValidator.validate_status_code(
        response,
        200
    )


@pytest.mark.xfail(reason="DummyJSON instability / HTTP 520 / timeouts on auth endpoints")
def test_invalid_login():

    response = auth_api.invalid_login()

    response_json = response.json()

    print(response.status_code)
    print(response_json)

    ResponseValidator.validate_status_code(
        response,
        400
    )