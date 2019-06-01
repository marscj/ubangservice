default_app_config = 'ubang.booking.apps.BookingConfig'

class BookingStatus:
    Created = 'Created'
    Process = 'Process'
    Complete = 'Complete'
    Cancel = 'Cancel'
    Delete = 'Delete'
    

    CHOICES = [
        (Created, 'Created'),
        (Process, 'Process'),
        (Complete, 'Complete'),
        (Cancel, 'Cancel'),
        (Delete, 'Delete'),
    ]