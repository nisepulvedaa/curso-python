from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime    

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nombre", default="")
    description = models.CharField(max_length=500, verbose_name="Descripcion", default="")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el", null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo", default="")
    content = RichTextField(verbose_name="Contenido", null=True, blank=True)
    image = models.ImageField(default="null", verbose_name="Imagen",upload_to="articles")
    public = models.BooleanField(verbose_name="¿Publicado?", null=True, blank=True)
    user = models.ForeignKey(User, verbose_name="Usuario", editable=False,on_delete=models.CASCADE, null=True, blank=True)
    categories = models.ManyToManyField(Category,verbose_name="Categorias",  blank=True,related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado el", null=True, blank=True)

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title