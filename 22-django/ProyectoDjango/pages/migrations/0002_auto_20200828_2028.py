# Generated by Django 3.1 on 2020-08-29 00:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Página', 'verbose_name_plural': 'Páginas'},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=0, verbose_name='orden'),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]