
default_app_config = 'ubang.order.apps.OrderConfig'

class OrderStatus:
    Draft = 0
    Confirm = 1
    Padding = 2
    Cancel = 3
    Complete = 4

    CHOICES = [
        (Draft, 'Draft'),
        (Padding, 'Padding'),
        (Confirm, 'Confirm'),
        (Cancel, 'Cancel'),
        (Complete, 'Complete')
    ]