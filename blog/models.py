from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False, unique=True, verbose_name='Nombre')

    def __str__(self):
        return "Categoría con Id %d y con nombre %s" % (self.id, self.nombre)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']  # si descendente: '-id'


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, unique=True, null=False, verbose_name='Título')
    contenido = models.TextField(null=True, verbose_name='Contenido del Post')
    imagen = models.ImageField(upload_to='posts/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen del Post')
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')
    fecha_actualizacion= models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
        super(Post, self).delete(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']  # si descendente: '-id'