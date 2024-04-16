from .models import Page
def ctx_pages(request):
    pages = Page.objects.all()
    dic = {"pages":[]}
    for i in pages:
        dic["pages"].append({"id":i.id,"title":i.title})
    return dic