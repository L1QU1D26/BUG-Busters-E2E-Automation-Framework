from api.Base.api_client import APIClient
from api.payloads.cart_payload import CartPayload


class CartAPI(APIClient):

    CART_ENDPOINT = "/carts/add"

    def add_valid_cart(self):

        payload = CartPayload.valid_cart_payload()

        response = self.post(
            self.CART_ENDPOINT,
            payload
        )

        return response

    def add_invalid_cart(self):

        payload = CartPayload.invalid_cart_payload()

        response = self.post(
            self.CART_ENDPOINT,
            payload
        )

        return response