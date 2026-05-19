import requests
from config.config import BASE_URL

class APIClient:

    def __init__(self):
        self.session = requests.Session()
        self.base_url = BASE_URL

    def get(self, endpoint, headers=None, params=None):
        response = self.session.get(
            url=f"{self.base_url}{endpoint}",
            headers=headers,
            params=params
        )
        return response

    def post(self, endpoint, payload=None, headers=None):
        response = self.session.post(
            url=f"{self.base_url}{endpoint}",
            json=payload,
            headers=headers
        )
        return response

    def put(self, endpoint, payload=None, headers=None):
        response = self.session.put(
            url=f"{self.base_url}{endpoint}",
            json=payload,
            headers=headers
        )
        return response

    def delete(self, endpoint, headers=None):
        response = self.session.delete(
            url=f"{self.base_url}{endpoint}",
            headers=headers
        )
        return response