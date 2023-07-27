from django.views import generic


class ListView(generic.ListView):
    pass


class DetailView(generic.DetailView):
    # These fields will be added to the context-data.
    fields = []
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        try:
            context['fields'] = self.fields
        except AttributeError:
            pass

        return context


class CreateView(generic.CreateView):
    pass


class UpdateView(generic.UpdateView):
    pass


class DeleteView(generic.DeleteView):
    pass


class DefaultsPrepopulateFilterSetMixin:
    """
    expects a constants defaults = {'field', 'value'}
    """

    def __init__(self, *args, **kwargs):
        # Prepopulate the filter to set approved first.
        super().__init__(*args, **kwargs)

        for k, v in self.defaults.items():
            self.form.initial[k] = v


class DefaultsPrepopulateFilterViewMixin:
    """
    expects a constants defaults = {'field', 'value'}
    """

    def get_filterset_kwargs(self, filterset_class):
        # Prepopulate the qs before a filter was clicked
        kwargs = super().get_filterset_kwargs(filterset_class)
        if kwargs['data'] is None:
            kwargs['queryset'] = kwargs['queryset'].filter(**self.defaults)
        return kwargs
