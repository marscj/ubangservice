from django.apps import AppConfig

class TaskConfig(AppConfig):
    name = 'ubang.task'
    
    def ready(self):
        import ubang.task.handler
        