from api.Base.api_client import APIClient

class ProductAPI(APIClient):

    PRODUCT_ENDPOINT = "/products"

    def get_all_products(self):

        response = self.get(
            self.PRODUCT_ENDPOINT
        )

        return response

    def get_single_product(self, product_id):

        response = self.get(
            f"{self.PRODUCT_ENDPOINT}/{product_id}"
        )

        return response
