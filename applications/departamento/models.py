from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Name', max_length=50, blank=True)
    short_name = models.CharField('Short Name', max_length=20, unique=True)
    anulated = models.BooleanField('Unactive', default=False)
    #fecha = models.DateField(, auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        unique_together = ('name', 'short_name')# no permite dobles registros

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name

