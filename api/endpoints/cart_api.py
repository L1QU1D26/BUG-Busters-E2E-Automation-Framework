from api.base.api_client import APIClient

class CartAPI(APIClient):

    CART_ENDPOINT = "/carts/add"

    def add_to_cart(self, user_id, product_id, quantity):

        payload = {
            "userId": user_id,
            "products": [
                {
                    "id": product_id,
                    "quantity": quantity
                }
            ]
        }

        response = self.post(
            self.CART_ENDPOINT,
            payload
        )

        return response