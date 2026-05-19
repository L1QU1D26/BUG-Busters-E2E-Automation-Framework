def order_payload(product_id, quantity):

    payload = {
        "products": [
            {
                "id": product_id,
                "quantity": quantity
            }
        ]
    }

    return payload