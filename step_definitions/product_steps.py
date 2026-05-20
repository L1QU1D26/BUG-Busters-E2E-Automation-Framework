from pages.product_page import ProductPage


class TestProduct:

    def test_add_product_to_cart(self, driver):

        product = ProductPage(driver)

        product.click_product()
        product.click_add_to_cart()

        assert product.get_cart_count() == "1"