from django.db import models

class empleado(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    file = models.IntegerField()
    def __srt__(self) -> str:
        return f'{self.name} || {self.email} || Nro legajo: {self.file}.'


class gerencia(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    def __srt__(self) -> str:
        return f'{self.name} || Función dentro de la empresa: {self.description}.'

class producto(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()

    def __srt__(self) -> str:
        return f'{self.name} || Precio: {self.price}.'