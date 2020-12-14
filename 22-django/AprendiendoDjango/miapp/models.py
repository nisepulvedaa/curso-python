from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="titulo")
    content = models.TextField(verbose_name="contenido")
    image = models.ImageField(default='null', verbose_name="imagen", upload_to="articles")
    public = models.BooleanField(verbose_name="es publico")
    create_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True,verbose_name="Editado")
    
    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['id']
    
    def __str__(self):
        publico = ""
        if self.public:
            publico += "(publicado)"
        else:
            publico  += "(privado)"    
        return "{}  {} ".format(self.title, publico)
    

class Category(models.Model):
    name =  models.CharField(max_length=110, verbose_name="nombre")
    description =models.CharField(max_length=250,verbose_name="descripcion")
    created_at = models.DateField()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
