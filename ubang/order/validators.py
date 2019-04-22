from django.core.exceptions import ValidationError

def customer_validator(customer):
    if customer.company is None:
        raise ValidationError('Ensure customer has company')