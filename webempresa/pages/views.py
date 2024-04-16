from django.shortcuts import render,get_object_or_404
from django.utils.text import slugify
from .models import Page
# Create your views here.

def page(request,page_title):
    todas_paginas = Page.objects.all()
    lista_slugificada = [slugify(item.title) for item in todas_paginas]
    id_solicitada = todas_paginas[0].id
    print(f"Inicial {id_solicitada}")
    try:
        id_solicitada = lista_slugificada.index(page_title)
        id_solicitada+=1
    except:
        pass
    print(f"encontro {id_solicitada} y pidio {lista_slugificada}")
    page = get_object_or_404(Page,id=id_solicitada)
    return render(request,"pages/sample.html",{"page":page}) #, "blogs":blog})
