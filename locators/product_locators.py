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

    PRODUCT_LINKS = (
        By.XPATH,
        "//a[contains(@href,'product.php')]"
    )

    PRODUCT_DETAIL_BODY = (
        By.TAG_NAME,
        "body"
    )

    FILTER_SECTION = (
        By.XPATH,
        "//*[contains(translate(@class,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'filter') "
        "or contains(translate(@id,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'filter') "
        "or contains(translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'filter')]"
    )

    ADD_TO_CART = (
        By.CLASS_NAME,
        "addToCart"
    )

    ADD_TO_CART_BUTTONS = (
        By.XPATH,
        "//button[contains(@class,'addToCart')]"
    )

    CART_ICON = (
        By.ID,
        "cartdesk"
    )

    CART_COUNT = (
        By.ID,
        "cartCount"
    )
