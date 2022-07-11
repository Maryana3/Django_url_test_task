import json
from django.core import serializers
from django.views.generic import ListView
from .models import Url


class MyView(ListView):
    template_name = 'home.html'
    queryset = Url.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return super().get_queryset()
        else:
            return user.urlset.url_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tmp = self.get_queryset()
        qs_json = serializers.serialize(
            'json', tmp)
        context['qs_json'] = qs_json
        return context
