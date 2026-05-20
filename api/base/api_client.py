import requests
from api.utils.logger import get_logger


class APIClient:

    logger = get_logger()

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, headers=None):

        url = self.base_url + endpoint

        self.logger.info(f"GET Request URL: {url}")

        response = requests.get(
            url,
            headers=headers
        )

        self.logger.info(f"Response Status Code: {response.status_code}")
        self.logger.info(f"Response Body: {response.text}")

        return response

    def post(self, endpoint, payload=None, headers=None):

        url = self.base_url + endpoint

        self.logger.info(f"POST Request URL: {url}")
        self.logger.info(f"Request Payload: {payload}")

        response = requests.post(
            url,
            json=payload,
            headers=headers
        )

        self.logger.info(f"Response Status Code: {response.status_code}")
        self.logger.info(f"Response Body: {response.text}")

        return response

    def put(self, endpoint, payload=None, headers=None):

        url = self.base_url + endpoint

        self.logger.info(f"PUT Request URL: {url}")
        self.logger.info(f"Request Payload: {payload}")

        response = requests.put(
            url,
            json=payload,
            headers=headers
        )

        self.logger.info(f"Response Status Code: {response.status_code}")
        self.logger.info(f"Response Body: {response.text}")

        return response

    def delete(self, endpoint, headers=None):

        url = self.base_url + endpoint

        self.logger.info(f"DELETE Request URL: {url}")

        response = requests.delete(
            url,
            headers=headers
        )

        self.logger.info(f"Response Status Code: {response.status_code}")
        self.logger.info(f"Response Body: {response.text}")

        return response