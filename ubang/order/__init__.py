
default_app_config = 'ubang.order.apps.OrderConfig'

class OrderStatus:
    Open = 'Open'
    Padding = 'Padding'
    Cancel = 'Cancel'
    Complete = 'Complete'
    Delete = 'Delete'

    CHOICES = [
        (Open, 'Open'),
        (Padding, 'Padding'),
        (Cancel, 'Cancel'),
        (Complete, 'Complete'),
        (Delete, 'Delete'),
    ]