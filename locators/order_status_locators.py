from selenium.webdriver.common.by import By


class OrderStatusLocators:
	PLACE_ORDER_BUTTON = (
		By.XPATH,
		"//a[normalize-space()='Place Order']"
	)

	THANK_YOU_MESSAGE = (
		By.XPATH,
		"//h1[contains(normalize-space(), 'Thank You for Your Order!') or contains(normalize-space(), 'Thank You for Your Order')]"
	)

	# Backward-compatible alias for success message if other tests reference it
	SUCCESS_MESSAGE = (
		By.XPATH,
		"//h1[contains(normalize-space(), 'Thank You for Your Order!') or contains(normalize-space(), 'Thank You for Your Order')]"
	)

	CONFIRM_PAGE_URL = "https://shop.qaautomationlabs.com/confirm.php"
	THANKS_PAGE_URL = "https://shop.qaautomationlabs.com/thanks.php"

