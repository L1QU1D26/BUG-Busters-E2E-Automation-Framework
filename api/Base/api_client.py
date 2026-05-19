import requests

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, headers=None):

        response = requests.get(
            self.base_url + endpoint,
            headers=headers
        )

        return response

    def post(self, endpoint, payload=None, headers=None):

        response = requests.post(
            self.base_url + endpoint,
            json=payload,
            headers=headers
        )

        return response

    def put(self, endpoint, payload=None, headers=None):

        response = requests.put(
            self.base_url + endpoint,
            json=payload,
            headers=headers
        )

        return response

    def delete(self, endpoint, headers=None):

        response = requests.delete(
            self.base_url + endpoint,
            headers=headers
        )

        return response