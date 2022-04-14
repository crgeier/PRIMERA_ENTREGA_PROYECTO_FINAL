import email
from multiprocessing import context
from typing import Any, Dict
from django.views.generic import TemplateView
from django.shortcuts import render
from empresa.models import *

class empresaView(TemplateView):
    template_name = 'forms/index.html'

    def post(self,request):
        name = request.POST['name']
        email = request.POST['email']
        file = request.POST['file']

        print(f'Nombre: {name}')
        print(f'Email: {email}')
        print(f'Legajo: {file}')

        obj_empleado = empleado(name=name, email=email, file=file)
        obj_empleado.save()

        return render(request,self.template_name)

class empresa2View(TemplateView):
    template_name = 'forms/index-gerencia.html'

    def post(self,request):
        name = request.POST['name']
        description = request.POST['description']
        
        print(f'Nombre: {name}')
        print(f'Descripción: {description}')
        
        obj_gerencia = gerencia(name=name, description=description)
        obj_gerencia.save()

        return render(request,self.template_name)
    
class empresa3View(TemplateView):
    template_name = 'forms/index-producto.html'

    def post(self,request):
        name = request.POST['name']
        price = request.POST['price']
        
        print(f'Nombre del Producto: {name}')
        print(f'Precio: {price}')
        
        obj_producto = producto(name=name, price=price)
        obj_producto.save()

        return render(request,self.template_name)

class SearchView(TemplateView):
    template_name = 'forms/search.html'

    def post(self, request):
        
        context = {
            "elements": producto.objects.filter(
                name=request.POST.get('name')
            )
        }
        return render(request,self.template_name, context)