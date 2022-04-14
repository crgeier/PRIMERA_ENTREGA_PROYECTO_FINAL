from typing import Any, Dict
from django.views.generic import TemplateView
from django.shortcuts import render

class empresaView(TemplateView):
    template_name = 'empresa/index.html'

    def get(self, request, status=None):
        context = {}
        return render(request, self.template_name, context)