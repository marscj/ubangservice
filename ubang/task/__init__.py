default_app_config = 'ubang.task.apps.TaskConfig'

class TaskPriceType:
    Vehicle = 0
    Guide = 1

    CHOICES = [
        (Vehicle, 'Vehicle'),
        (Guide, 'Guide')
    ]