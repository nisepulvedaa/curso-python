from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login_page")
def list(request):
    #sacar articulos
    articulos =  Article.objects.all() 

    #Paginar los articulos
    paginator = Paginator(articulos, 2)

    #recoger numero pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)


    return render(request,'articles/list.html', {
        'title':'Artículos',
        'articulos':page_articles
})

@login_required(login_url="login_page")
def category(request,category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category_id)
    return render(request,'categories/category.html',{
        'category':category,
        'articulos':articles
})

@login_required(login_url="login_page")
def article(request,article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detalle.html',{
        'article':article
    })