from django.shortcuts import render,HttpResponse

# Create your views here.
httpHeader='''

<ul>
<li> <a href='/' >Home</a></li>
<li> <a href='/about' >Historia</a></li>
<li> <a href='/services' >Servicios</a></li>
<li> <a href='/store' >Visítanos</a></li>
<li> <a href='/contact' >Contacto</a></li>
<li> <a href='/blog' >Blog</a></li>
<li> <a href='/sample' >Sample</a></li>
</ul>
'''

def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def services(request):
    return render(request,"core/services.html")

def store(request):
    return render(request,"core/store.html")

def contact(request):
    return render(request,"core/contact.html")

def blog(request):
    return render(request,"core/blog.html")

def sample(request):
    respuesta=httpHeader+"<h1>Sample</h1>"
    return HttpResponse(respuesta)