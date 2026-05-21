from selenium.webdriver.common.by import By


class NavigationLocators:

    # Shop dropdown
    SHOP_MENU = (
        By.CLASS_NAME,
        "dropdown-toggle"
    )

    # Dropdown categories
    MENS_WEAR = (
        By.XPATH,
        "//a[@href='mens-wear.php']"
    )

    WOMENS_WEAR = (
        By.XPATH,
        "//a[@href='womens-wear.php']"
    )

    KIDS_WEAR = (
        By.XPATH,
        "//a[@href='kids-wear.php']"
    )

    ELECTRONICS = (
        By.XPATH,
        "//a[@href='electronics.php']"
    )

    # Cart icon
    CART_ICON = (
        By.ID,
        "cartdesk"
    )

    # Back button
    GO_BACK = (
        By.XPATH,
        "//a[contains(text(),'Go To Back')]"
    )