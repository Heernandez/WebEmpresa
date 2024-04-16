from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):
    #print(f"Tipo de peticion {request.method}")
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name","")
            email = request.POST.get("email","")
            content = request.POST.get("content","")
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", #asunto
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content), #cuerpo
                "no-contestar@inbox.mailtrap.io", #origen
                ["luishernandez@utp.edu.co"], #destino
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contactPage')+"?ok")
            except:
                return redirect(reverse('contactPage')+"?fail")
            # Enviamos correo y redireccionamos
            #return redirect("/contact/ok?")
    return render(request,"contact/contact.html",{"form":contact_form})