from api.base.api_client import APIClient

class AuthAPI(APIClient):

    LOGIN_ENDPOINT = "/auth/login"

    def login(self, username, password):

        payload = {
            "username": username,
            "password": password
        }

        response = self.post(
            self.LOGIN_ENDPOINT,
            payload
        )

        return response