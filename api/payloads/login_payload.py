class LoginPayload:

    @staticmethod
    def valid_login_payload():
        return {
            "username": "emilys",
            "password": "emilyspass"
        }

    @staticmethod
    def invalid_login_payload():
        return {
            "username": "wrong_user",
            "password": "wrong_password"
        }