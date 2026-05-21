from selenium.webdriver.common.by import By


class NavigateLocators:
    PRODUCTS_MENU = (By.CSS_SELECTOR, ".nav-link.dropdown-toggle")
    VIEW_ALL_PRODUCTS = (By.CSS_SELECTOR, ".dropdown-menu a[href='shop.php']")
    CART_ICON = (By.ID, "cartdesk")
    PRODUCT_CATEGORY = (
        By.XPATH,
        "//a[contains(@href,'mens-wear.php') and contains(.,'Shop Now')]",
    )
