Widget Online Sales Application - Exception Handling Framework

This project provides a structured exception-handling framework for the backend of a Widget online sales application. It ensures clear communication of errors to users, detailed internal logging for debugging, and appropriate HTTP status codes for various error scenarios.

Features

Custom Exception Hierarchy:
A well-organized class structure for all exceptions, including:
WidgetException: Base class for all exceptions.
SupplierException: For supplier-related issues.
CheckoutException: For checkout-related problems.
Specific Exception Types:
Supplier Exceptions:
NotManufacturedAnymoreException
ProductionDelayedException
ShippingDelayedException
Checkout Exceptions:
Inventory:
OutOfStockException
Pricing:
InvalidCouponCodeException
CannotStackCouponsException
Error Messaging:
Separate internal error messages for logging and user-friendly error messages for clients.
HTTP Status Codes:
500: For server-side errors (e.g., inventory or supplier issues).
400: For client-side errors (e.g., invalid or conflicting coupon codes).
Logging:
Captures and logs:
Exception type.
Timestamp.
Internal error message.
Full traceback for debugging.
User-Facing JSON Responses:
Returns clear, standardized JSON responses for API clients, including:
http_status: The HTTP error code.
error: The user-friendly error message.
