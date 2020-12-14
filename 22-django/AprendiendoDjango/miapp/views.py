from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

layout = """
<h1>Sitio web con Django | Nicolas Sepulveda </h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de Pruebas</a>
    </li>
     <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr/>
"""


def index(request):
    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    ""

    year = 2020

    while year <=2050:
        if year % 2 == 0:
            html += "<li>{}</li>".format(str(year))
     
        year += 1

    html += "</ul>"
    """

    year = 2020
    hasta = range(2020,2051)

    nombre = 'Nicolas Sepulveda'
    lenguajes = ['Javascript','Python', 'PHP','C']
    #lenguajes = []
    return render(request, 'index.html',{
        'title':'Inicio',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })
    #return HttpResponse(layout+html)

def hola_mundo(request):
    return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):

    if redirigir == 1:
        #return redirect('/contacto/Nicolas/Sepulveda')
        return redirect('contacto',nombre="Nicolas",apellidos="Sepulveda")

    return render(request, 'pagina.html',{
        'texto':'asdasa',
        'lista': ['uno','dos','tres']
    })

def contacto(request,nombre="", apellidos=""):

    html = ""
  

    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += " <h3>{} {} </h3> ".format(nombre,apellidos)

    return HttpResponse(layout+"<h2>contacto </h2>" + html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public =  public
    )

    articulo.save()
    return HttpResponse("Articulo Creado: <strong>{}</strong> - {} ".format(articulo.title,articulo.content))

def save_article(request):
    """
    if request.method == "GET":
        title = request.GET['title']
        if len(title) <= 5:
           return HttpResponse("<h2>El titulo es muy pequeño</h2>")
        content = request.GET['content']
        public = request.GET['public']
        articulo = Article(
            title = title,
            content = content,
            public =  public
        )
    """
    if request.method == "POST":
        title = request.POST['title']
        if len(title) <= 5:
           return HttpResponse("<h2>El titulo es muy pequeño</h2>")
        content = request.POST['content']
        public = request.POST['public']
        articulo = Article(
            title = title,
            content = content,
            public =  public
        )
        articulo.save()
        return HttpResponse("Articulo Creado: <strong>{}</strong> - {} ".format(articulo.title,articulo.content))
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

   

def create_article(request):
    return render(request, 'create_article.html')

def create_full_article(request):

    if request.method == "POST":
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form.get('title') 
            content = data_form['content']
            public = data_form['public']
            grabarArticulo(request,title,content,public)
           
            return redirect('articulos')
            #return HttpResponse("{} - {} - {} ".format(title,content,str(public)) )
    else:
        formulario = FormArticle()
   

    return render(request, 'create_full_article.html', {
        'formulario': formulario
    })

def articulo(request):
    response = "";
    try:
        articulo = Article.objects.get(title="Quinto articulo", public=True)
        response +="Articulo: <br /> {} {} ".format(articulo.id,articulo.title)
    except:
            response +="<h1>Articulo no econtrado</h1> "

    return HttpResponse(response);

def editar_articulo(request,id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Tercer Articulo"
    articulo.content = "Contenido del Tercer Articulo"
    articulo.public = True

    articulo.save()

    return HttpResponse("Articulo: <br /> {} {} ".format(articulo.id,articulo.title));

def articulos(request):
    articulos = Article.objects.all()
    #articulos = Article.objects.order_by('id')[0:4]
    #articulos = Article.objects.filter(title="Tercer Articulo", id=3)
    #articulos = Article.objects.filter(title__exact="Tercer Articulo")
    #articulos = Article.objects.filter(title__contains="rticulo")
    #articulos = Article.objects.filter(title__iexact="articulo",)
    #articulos = Article.objects.filter(id__gt=9)
    #articulos = Article.objects.filter(id__gte=9)
    #articulos = Article.objects.filter(id__lt=9)
    #articulos = Article.objects.filter(id__lte=9)
    #articulos = Article.objects.filter(title__contains="Articulo", public=True).exclude(content__contains="vacio")
    #articulos = Article.objects.raw("SELECT * FROM miapp_article where title = 'Articulo 8' and public = 0 ")
    #articulos = Article.objects.filter(Q(title__contains="2")|Q(title__contains="3"))
    #articulos = Article.objects.filter(Q(title__contains="2")|Q(public=True))
    
    return render(request, 'articulos.html',{
        'articulos':articulos
    })

def borrar_articulos(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')

def grabarArticulo(request,title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public =  public
    )

    articulo.save()
    #crear mesaje flash (sesión que solo se muestra 1 vez)
    messages.success(request, 'has creado correctamente el articulo {} '.format(articulo.id))

    