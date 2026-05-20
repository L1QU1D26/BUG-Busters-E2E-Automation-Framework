from api.endpoints.auth_api import AuthAPI
from api.validations.response_validator import ResponseValidator
from config.config import BASE_URL

auth_api = AuthAPI(BASE_URL)

def test_valid_login():

    response = auth_api.login(
        "emilys",
        "emilyspass"
    )

    response_json = response.json()

    print(response.status_code)
    print(response_json)

    ResponseValidator.validate_status_code(
        response,
        200
    )

    ResponseValidator.validate_response_time(
        response,
        5
    )

    ResponseValidator.validate_key(
        response_json,
        "accessToken"
    )


def test_invalid_login():

    response = auth_api.login(
        "wrong_user",
        "wrong_password"
    )

    response_json = response.json()

    print(response.status_code)
    print(response_json)

    ResponseValidator.validate_status_code(
        response,
        400
    )