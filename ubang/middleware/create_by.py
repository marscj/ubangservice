from django import conf
from django.db.models import signals
from django.core.exceptions import FieldDoesNotExist
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import curry

class WhoDidMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method not in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
            print(request)
            if hasattr(request, 'user') and request.user.is_authenticated:
                user = request.user
                print(user)
            else:
                user = None
                print(user)

            mark_whodid = curry(self.mark_whodid, user)
            signals.pre_save.connect(mark_whodid, dispatch_uid=(self.__class__, request,), weak=False)

    def process_response(self, request, response):
        if request.method not in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
            signals.pre_save.disconnect(dispatch_uid=(self.__class__, request,))
        return response

    def mark_whodid(self, user, sender, instance, **kwargs):
        create_by_field, update_by_field, company_by_field = conf.settings.CREATE_BY_FIELD, conf.settings.UPDATE_BY_FIELD, conf.settings.COMPANY_BY_FIELD
        
        try:
            instance._meta.get_field(create_by_field)
        except FieldDoesNotExist:
            pass
        else:
            if not getattr(instance, create_by_field):
                setattr(instance, create_by_field, user)

        try:
            instance._meta.get_field(update_by_field)
        except FieldDoesNotExist:
            pass
        else:
            setattr(instance, update_by_field, user)

        try:
            instance._meta.get_field(company_by_field)
        except FieldDoesNotExist:
            pass
        else:
            if not getattr(instance, company_by_field) and user is not None and user.company is not None:
                setattr(instance, company_by_field, user.company)
