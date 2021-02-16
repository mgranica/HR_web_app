from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades de Empleado'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


# Create your models here.
class Empleado(models.Model):
    """
    Modelo para tabla empleado
    """
    job_choices = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    first_name = models.CharField('Name', max_length=60)
    last_name = models.CharField('Last Name', max_length=60)
    full_name = models.CharField(
        'Full Name', 
        max_length=120,
        blank=True
    )
    job = models.CharField('Job', max_length=1, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField(blank=True)

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Recursos Humanos'
        ordering = ['last_name']
        unique_together = ('first_name', 'departamento')# no permite dobles registros

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
