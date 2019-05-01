
default_app_config = 'ubang.order.apps.OrderConfig'

class OrderStatus:
    Open = 0
    Padding = 1
    Cancel = 2
    Complete = 3
    Close = 4

    CHOICES = [
        (Open, 'Open'),
        (Padding, 'Padding'),
        (Cancel, 'Cancel'),
        (Complete, 'Complete'),
        (Close, 'Close'),
    ]