========================================
BUG Busters - API Feature Documentation
========================================

Module Name: Authentication API
Feature File: login_api.feature
API Type: POST
Endpoint: /api/login

Scenarios Covered:
--------------------------------------------------

1. Verify successful login with valid credentials
   - Validate status code 200
   - Validate auth token generation

2. Verify login with invalid password
   - Validate status code 401
   - Validate error message

3. Verify login with empty email field
   - Validate required field validation

4. Verify login with empty password field
   - Validate required field validation

5. Verify login with invalid email format
   - Validate validation message

==================================================

Module Name: Product API
Feature File: products_api.feature
API Type: GET
Endpoint: /api/products

Scenarios Covered:
--------------------------------------------------

1. Verify all products are fetched successfully
2. Verify product details by valid product ID
3. Verify product details with invalid product ID
4. Verify unauthorized access without token

==================================================

Module Name: Cart API
Feature File: cart_api.feature
API Type: POST / GET
Endpoint: /api/cart

Scenarios Covered:
--------------------------------------------------

1. Verify product added to cart successfully
2. Verify cart item count updated
3. Verify duplicate product handling
4. Verify cart retrieval
5. Verify unauthorized cart access

==================================================

Module Name: Orders API
Feature File: orders_api.feature
API Type: POST / GET
Endpoint: /api/orders

Scenarios Covered:
--------------------------------------------------

1. Verify order creation successfully
2. Verify order details retrieval
3. Verify order creation with invalid payload
4. Verify payment validation
5. Verify unauthorized order access

==================================================

# BUG Busters API Feature Traceability

## Authentication API

Feature File: `login_api.feature`

| Scenario ID | Scenario Name | Endpoint | Method |
|---|---|---|---|
| AUTH_001 | Valid Login | /api/login | POST |
| AUTH_002 | Invalid Password | /api/login | POST |
| AUTH_003 | Empty Email | /api/login | POST |

---

## Cart API

Feature File: `cart_api.feature`

| Scenario ID | Scenario Name | Endpoint | Method |
|---|---|---|---|
| CART_001 | Add Product to Cart | /api/cart | POST |
| CART_002 | Get Cart Details | /api/cart | GET |