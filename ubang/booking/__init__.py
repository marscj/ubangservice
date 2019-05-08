default_app_config = 'ubang.booking.apps.BookingConfig'

class BookingStatus:
    Darft = 0
    Confirm = 1
    Cancel = 2
    Delete = 3

    CHOICES = [
        (Darft, 'darf'),
        (Confirm, 'confirm'),
        (Cancel, 'cancel'),
        (Delete, 'delete')
    ]