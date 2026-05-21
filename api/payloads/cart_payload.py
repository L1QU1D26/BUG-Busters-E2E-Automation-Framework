class CartPayload:

    @staticmethod
    def valid_cart_payload():
        return {
            "userId": 1,
            "products": [
                {
                    "id": 1,
                    "quantity": 2
                }
            ]
        }

    @staticmethod
    def invalid_cart_payload():
        return {
            "userId": "",
            "products": [
                {
                    "id": "",
                    "quantity": ""
                }
            ]
        }