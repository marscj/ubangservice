from django.contrib import admin

class InputFilter(admin.SimpleListFilter):
    template = 'input_filter/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v) for k, v in changelist.get_filters_params().items() if k != self.parameter_name
        )

        for k, v in changelist.get_filters_params().items():
            print(k,v)

        yield all_choice