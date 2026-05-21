from selenium.webdriver.common.by import By


class CheckoutLocators:
    PROCEED_TO_CHECKOUT = (
        By.ID,
        "checkoutBtn"
    )

    FIRST_NAME = (
        By.ID,
        "firstname"
    )

    MIDDLE_NAME = (
        By.ID,
        "middlename"
    )

    LAST_NAME = (
        By.ID,
        "lastname"
    )

    EMAIL = (
        By.ID,
        "email"
    )

    PHONE = (
        By.ID,
        "phone"
    )

    ADDRESS = (
        By.ID,
        "address"
    )

    STATE = (
        By.ID,
        "states"
    )

    CITY = (
        By.ID,
        "city"
    )

    PINCODE = (
        By.ID,
        "pincode"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//a[normalize-space()='Place Order']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//p[contains(normalize-space(), 'Your order has been placed successfully.')]"
    )

    ERROR_MESSAGES = (
        By.CSS_SELECTOR,
        ".form-control + p"
    )

    CART_PAGE_URL = "https://shop.qaautomationlabs.com/cart.php"
    CHECKOUT_PAGE_URL = "https://shop.qaautomationlabs.com/checkout.php"
    CONFIRM_PAGE_URL = "https://shop.qaautomationlabs.com/confirm.php"
    THANKS_PAGE_URL = "https://shop.qaautomationlabs.com/thanks.php"
