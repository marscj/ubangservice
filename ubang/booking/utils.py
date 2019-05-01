
from decimal import Decimal

def save_discount(booking, company):
    
    if company and company.discount:
        booking.discount_name = company.discount.name
        booking.discount_value = company.discount.value
    else:
        booking.discount_name = 'no discount'
        booking.discount_value = Decimal(0.0)
