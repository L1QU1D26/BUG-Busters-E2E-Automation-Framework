from selenium.webdriver.common.by import By


class ProductLocators:

    MEN_FASHION_SHOP_NOW = (
        By.XPATH,
        "(//a[contains(text(),'Shop Now')])[1]"
    )

    FIRST_PRODUCT_NAME = (
        By.XPATH,
        "(//a[contains(@href,'product.php')])[1]"
    )

    ADD_TO_CART = (
        By.CLASS_NAME,
        "addToCart"
    )

    CART_ICON = (
        By.ID,
        "cartdesk"
    )

    CART_COUNT = (
        By.ID,
        "cartCount"
    )