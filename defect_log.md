# 🐛 Defect Log & Analysis Report

This document records the defects discovered, analyzed, and resolved during the Wipro Capstone project E2E Test Automation Framework implementation.

---

## Defect Summary Dashboard

| Defect ID | Description | Severity | Component | Root Cause | Status |
|-----------|-------------|----------|-----------|------------|--------|
| **BUG-001** | E2E test suite hangs indefinitely on invalid API payloads | Critical | API Framework | Missing HTTP timeout configuration on requests | **Resolved** |
| **BUG-002** | BDD Step definitions crash with `AttributeError` on Men's Category | Major | UI Step Definitions | Missing POM reference `open_mens_wear_category()` | **Resolved** |
| **BUG-003** | Product selection fails due to missing parameters | Major | UI Page Objects | Missing product index argument in page action | **Resolved** |
| **BUG-004** | Left-panel filters do not toggle when clicking checkbox inputs | Medium | UI Page Objects | custom CSS styles overlay and block input interaction | **Resolved** |
| **BUG-005** | Invalid cart and order payloads trigger HTTP 520 server errors | Low | External API | Mock server crashes and fails validation handling | **Handled (XFail)** |

---

## Detailed Defect Analysis

### BUG-001: Infinite Hang in API Test Suite
- **Component**: `api/Base/api_client.py`
- **Severity**: Critical
- **Symptoms**: The entire test runner hung in CI/CD and local environments, requiring a manual kill of the processes.
- **Root Cause**: The Python `requests` library blocks indefinitely if a connection is accepted but no response is sent. When invalid payloads were posted to DummyJSON, Cloudflare WAF rate-limiting or security shields dropped the packets without responding, causing the suite to hang.
- **Remediation**:
  1. Updated `APIClient` methods (`get`, `post`, `put`, `delete`) to enforce a `timeout=10` constraint.
  2. Implemented `urllib3` retry logic with standard backoff to handle transient 500, 502, 503, 504, and 520 status codes.
- **Status**: **Resolved**

### BUG-002: AttributeError in BDD Step Definitions
- **Component**: `step_definitions/test_checkout.py` and `step_definitions/test_order_status.py`
- **Severity**: Major
- **Symptoms**: Pytest-BDD failed to compile tests, throwing:
  `AttributeError: 'ProductPage' object has no attribute 'open_mens_wear_category'`
- **Root Cause**: A POM refactoring renamed navigation helpers but the corresponding step definition files were not updated.
- **Remediation**:
  1. Replaced the non-existent method call with the generic, parameterized helper `open_category("Mens Wear")`.
- **Status**: **Resolved**

### BUG-003: Missing Parameter in Product Cart Action
- **Component**: `step_definitions/test_cart.py`
- **Severity**: Major
- **Symptoms**: `TypeError: add_product_to_cart() missing 1 required positional argument: 'index'`
- **Root Cause**: The underlying page object method required a 0-indexed product identifier to support dynamic multi-product clicks, but the step definition did not supply one.
- **Remediation**:
  1. Modified the step definition to call `add_product_to_cart(1)` to target the primary available product.
- **Status**: **Resolved**

### BUG-004: UI Left-Panel Filters Non-Clickable
- **Component**: `pages/product_page.py`
- **Severity**: Medium
- **Symptoms**: Selenium clicked the checkbox element, but the filter state did not toggle, and products on the shop page did not filter.
- **Root Cause**: The e-commerce frontend uses styled HTML overlays where the actual `<input type="checkbox">` is hidden via styling. Clicking the input had no effect since the surrounding `<label>` tag is the element capturing click events.
- **Remediation**:
  1. Updated the dynamic XPath generator to target and click the `<label>` tag directly: `//label[contains(text(), '{filter_name}')]`.
- **Status**: **Resolved**

### BUG-005: Mock Server Internal Crash (HTTP 520)
- **Component**: `tests/api/test_cart_api.py` and `tests/api/test_order_api.py`
- **Severity**: Low (External service dependency)
- **Symptoms**: API validation test cases for invalid bodies failed due to unexpected `520 Server Error`.
- **Root Cause**: The DummyJSON mock service has limited input validation; posting empty strings inside fields caused the remote Node.js backend to throw an unhandled exception, causing Cloudflare to return HTTP 520.
- **Remediation**:
  1. Configured `@pytest.mark.xfail` on negative test scenarios to mark them as expected failures without failing the overall suite.
- **Status**: **Handled**
