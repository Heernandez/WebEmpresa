from .models import Link
def ctx_dict(request):
    links = Link.objects.all()
    #ctx = {"test":"hola","links":link}
    ctx = {}
    for link in links:
        ctx[link.key] = link.url
    return ctx