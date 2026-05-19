from api.base.api_client import APIClient
from api.payloads.login_payload import login_payload

class AuthAPI(APIClient):

    LOGIN_ENDPOINT = "/auth/login"

    def login(self, username, password):

        payload = login_payload(username, password)

        headers = {
            "Content-Type": "application/json"
        }

        response = self.post(
            self.LOGIN_ENDPOINT,
            payload,
            headers
        )

        return response