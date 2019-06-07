
default_app_config = 'ubang.order.apps.OrderConfig'

class OrderStatus:
    Created = 'Created'
    Cancel = 'Cancel'
    Complete = 'Complete'
    # Delete = 'Delete'

    CHOICES = [
        (Created, 'Created'),
        (Cancel, 'Cancel'),
        (Complete, 'Complete'),
        # (Delete, 'Delete'),
    ]