from selenium.webdriver.common.by import By


class ProductLocators:

    # Category buttons
    MEN_FASHION_SHOP_NOW = (
        By.XPATH,
        "(//a[contains(text(),'Shop Now')])[1]"
    )

    WOMEN_FASHION_SHOP_NOW = (
        By.XPATH,
        "(//a[contains(text(),'Shop Now')])[2]"
    )

    KIDS_FASHION_SHOP_NOW = (
        By.XPATH,
        "(//a[contains(text(),'Shop Now')])[3]"
    )

    ELECTRONICS_SHOP_NOW = (
        By.XPATH,
        "(//a[contains(text(),'Shop Now')])[4]"
    )

    # Product
    FIRST_PRODUCT_NAME = (
        By.XPATH,
        "(//a[contains(@href,'product.php')])[1]"
    )

    PRODUCT_LIST = (
        By.ID,
        "product-list"
    )
    PRODUCT_CARDS = (
        By.CSS_SELECTOR,
        "div.product-item.bg-light.mb-4"
    )

    # Cart
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

    # Filters / dropdowns
    SORT_DROPDOWN = (
        By.TAG_NAME,
        "select"
    )