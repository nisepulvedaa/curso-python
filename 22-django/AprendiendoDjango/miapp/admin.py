from django.contrib import admin
from .models import Article,Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at','update_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)



#Configurar el titulo del panel 
title = "Master en Python - Nicolas Sepulveda"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Gestion" 