default_app_config = 'ubang.booking.apps.BookingConfig'

class BookingStatus:
    Darft = 'Darft'
    Confirm = 'Confirm'
    Cancel = 'Cancel'
    Delete = 'Delete'

    CHOICES = [
        (Darft, 'Darft'),
        (Confirm, 'Confirm'),
        (Cancel, 'Cancel'),
        (Delete, 'Delete')
    ]