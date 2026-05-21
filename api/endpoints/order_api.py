from api.Base.api_client import APIClient
from api.payloads.order_payload import OrderPayload


class OrderAPI(APIClient):

    ORDER_ENDPOINT = "/carts/add"

    def create_valid_order(self):

        payload = OrderPayload.valid_order_payload()

        response = self.post(
            self.ORDER_ENDPOINT,
            payload
        )

        return response

    def create_invalid_order(self):

        payload = OrderPayload.invalid_order_payload()

        response = self.post(
            self.ORDER_ENDPOINT,
            payload
        )

        return response