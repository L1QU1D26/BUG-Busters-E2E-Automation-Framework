class OrderPayload:

    @staticmethod
    def valid_order_payload():
        return {
            "userId": 1,
            "products": [
                {
                    "id": 1,
                    "quantity": 1
                }
            ]
        }

    @staticmethod
    def invalid_order_payload():
        return {
            "userId": "",
            "products": [
                {
                    "id": "",
                    "quantity": ""
                }
            ]
        }