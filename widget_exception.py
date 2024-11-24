import json
import traceback
from datetime import datetime
from http import HTTPStatus


class WidgetException(Exception):
    """Base class for all Widget application exceptions"""
    message="Generic Widget excetion."
    http_status=HTTPStatus.INTERNAL_SERVER_ERROR
    def __init__(self,*args,customer_message=None):
        super().__init__(*args)
        if args:
            self.message=args[0]
        self.customer_mesage=customer_message if customer_message is not None else self.message

    
    @property
    def traceback(self):
        return traceback.TracebackException.from_exception(self).format()


    def log_exception(self):
        """Logs exception details"""
        log_message={
            "timestamp": datetime.now().isoformat(),
            "type": type(self).__name__,
            "message": self.message,
            "args": self.args[1:],
            "traceback": list(self.traceback)
        }

        print(f"LOG: {datetime.now().isoformat()}: {log_message}")

    def to_json(self):
        """Returns a JSON representation of the user-facing error."""

        response={
            'code': self.http_status.value,
            'message': '{}: {}' .format(self.http_status.phrase,self.customer_mesage),
            'category': type(self).__name__,
            'time_utc': datetime.now().isoformat()
        }
        return json.dumps(response)
    
    

#Supplier exceptions

class SupplierException(WidgetException):
    """Base class for supplier-related exceptions."""
    message="Supplier exception"
    http_status=HTTPStatus.INTERNAL_SERVER_ERROR


class NotManufacturedAnymoreException(SupplierException):
    message='The widget is not manufactured by supplier anymore.'
    http_status=HTTPStatus.INTERNAL_SERVER_ERROR


class ProductionDelayedException(SupplierException):
    message='Widget production has been delayed'
    http_status=HTTPStatus.INTERNAL_SERVER_ERROR


class ShipmentDelayedException(SupplierException):
    message='Shipment of widget has been delayed.'
    http_status=HTTPStatus.INTERNAL_SERVER_ERROR

#Checkout exceptions
class CheckoutException(WidgetException):
    """Base class for checkout-related exceptions."""
    message='Checkout exception'
    http_status=HTTPStatus.INTERNAL_SERVER_ERROR


#Inventory exceptions
class InventoryException(CheckoutException):
    """Base class for inventory-related exceptions."""
    message='Inventory checkout exception'
    http_status=HTTPStatus.INTERNAL_SERVER_ERROR


class OutOfStockException(InventoryException):
    message='Inventory out of stock'
    http_status=HTTPStatus.INSUFFICIENT_STORAGE


#Pricing exceptions
class PricingException(CheckoutException):
    """Base class for pricing-related exceptions."""
    message='Inventory pricing exception'
    http_status=HTTPStatus.INTERNAL_SERVER_ERROR


class InvalidCouponCodeException(PricingException):
    message='Invalid checkout coupon code'
    http_status=HTTPStatus.BAD_REQUEST

class CannotStackCouponsException(PricingException):
    message='Cannot stack checkout coupon codes'
    http_status=HTTPStatus.BAD_REQUEST
    
if __name__== "__main__":
    try:
        raise ValueError
    except ValueError:
        try:
            raise InvalidCouponCodeException('User tried to use an old coupon',customer_message='This coupon has expired.')
        except InvalidCouponCodeException as ex:
            ex.log_exception()
            print('-------------')
            print(ex.to_json())
            print('--------------')
            print(''.join(ex.traceback))