default_app_config = 'ubang.booking.apps.BookingConfig'

class BookingStatus:
    Created = 'Created'
    Cancel = 'Cancel'
    Delete = 'Delete'
    Process = 'Process'
    Complete = 'Complete'
    

    CHOICES = [
        (Created, 'Created'),
        (Cancel, 'Cancel'),
        (Delete, 'Delete'),
        (Process, 'Complete'),
        (Complete, 'Complete')
    ]