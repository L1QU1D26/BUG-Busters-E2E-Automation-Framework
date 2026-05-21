import requests
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from api.utils.logger import get_logger


class APIClient:

    logger = get_logger()

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        
        # Configure retry strategy for resilient API testing
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504, 520],
            allowed_methods=["GET", "POST", "PUT", "DELETE"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def get(self, endpoint, headers=None):

        url = self.base_url + endpoint

        self.logger.info(f"GET Request URL: {url}")

        response = self.session.get(
            url,
            headers=headers,
            timeout=10
        )

        self.logger.info(f"Response Status Code: {response.status_code}")
        self.logger.info(f"Response Body: {response.text}")

        return response

    def post(self, endpoint, payload=None, headers=None):

        url = self.base_url + endpoint

        self.logger.info(f"POST Request URL: {url}")
        self.logger.info(f"Request Payload: {payload}")

        response = self.session.post(
            url,
            json=payload,
            headers=headers,
            timeout=10
        )

        self.logger.info(f"Response Status Code: {response.status_code}")
        self.logger.info(f"Response Body: {response.text}")

        return response

    def put(self, endpoint, payload=None, headers=None):

        url = self.base_url + endpoint

        self.logger.info(f"PUT Request URL: {url}")
        self.logger.info(f"Request Payload: {payload}")

        response = self.session.put(
            url,
            json=payload,
            headers=headers,
            timeout=10
        )

        self.logger.info(f"Response Status Code: {response.status_code}")
        self.logger.info(f"Response Body: {response.text}")

        return response

    def delete(self, endpoint, headers=None):

        url = self.base_url + endpoint

        self.logger.info(f"DELETE Request URL: {url}")

        response = self.session.delete(
            url,
            headers=headers,
            timeout=10
        )

        self.logger.info(f"Response Status Code: {response.status_code}")
        self.logger.info(f"Response Body: {response.text}")

        return response