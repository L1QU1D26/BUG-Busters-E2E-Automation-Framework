from api.base.api_client import APIClient
from api.payloads.order_payload import order_payload

class OrderAPI(APIClient):

    ORDER_ENDPOINT = "/carts/add"

    def create_order(self, product_id, quantity):

        payload = order_payload(
            product_id,
            quantity
        )

        headers = {
            "Content-Type": "application/json"
        }

        response = self.post(
            self.ORDER_ENDPOINT,
            payload,
            headers
        )

        return response