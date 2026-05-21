from api.Base.api_client import APIClient
from api.payloads.login_payload import LoginPayload


class AuthAPI(APIClient):

    LOGIN_ENDPOINT = "/auth/login"

    def valid_login(self):

        payload = LoginPayload.valid_login_payload()

        response = self.post(
            self.LOGIN_ENDPOINT,
            payload
        )

        return response

    def invalid_login(self):

        payload = LoginPayload.invalid_login_payload()

        response = self.post(
            self.LOGIN_ENDPOINT,
            payload
        )

        return response