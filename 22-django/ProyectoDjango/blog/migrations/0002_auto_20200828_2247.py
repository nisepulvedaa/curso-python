# Generated by Django 3.1 on 2020-08-29 02:47

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.Category', verbose_name='Categorias'),
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido'),
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to='', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='article',
            name='public',
            field=models.BooleanField(blank=True, null=True, verbose_name='¿Publicado?'),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=150, verbose_name='Titulo'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='', max_length=500, verbose_name='Descripcion'),
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Editado el'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
    ]
