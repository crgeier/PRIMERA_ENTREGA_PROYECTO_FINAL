from django.urls import path
from empresa2.views import *
from django.views.generic import TemplateView

app_name = "users"
urlpatterns = [
    path("", TemplateView.as_view(template_name="empresa2/index.html"), name="empresa2"),
    path("empresa2/", TemplateView.as_view(template_name="empresa2/home.html"), name="empresa2"),
        # path("empresa/", empresaView.as_view(), name="empresa2"),
    path("formulario/", empresaView.as_view(), name="formulario"),
    path("formulario1/", empresa2View.as_view(), name="formulario-gerencia"),
    path("formulario2/", empresa3View.as_view(), name="formulario-producto"),
    path("search/",SearchView.as_view(), name="search")
]