from selenium.webdriver.common.by import By


class CartLocators:

    SHOP_MENU = (
        By.LINK_TEXT,
        "Shop"
    )

    CATEGORY_LINK_TEXT = (
        By.LINK_TEXT,
        ""
    )

    ADD_TO_CART_BUTTON = (
    By.XPATH,
    ""
    )
    
    CART_ICON = (
        By.XPATH,
        "//a[contains(@href,'cart.php')]"
    )

    QUANTITY_INPUT = (
        By.XPATH,
        "(//input[@type='number'])[1]"
    )

    REMOVE_BUTTON = (
        By.XPATH,
        "(//button[contains(@class,'remove')])[1]"
    )

    CART_COUNT = (
        By.ID,
        "cartCount"
    )