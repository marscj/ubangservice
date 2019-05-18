default_app_config = 'ubang.booking.apps.BookingConfig'

class BookingStatus:
    Created = 'Created'
    Cancel = 'Cancel'
    Delete = 'Delete'

    CHOICES = [
        (Created, 'Created'),
        (Cancel, 'Cancel'),
        (Delete, 'Delete')
    ]