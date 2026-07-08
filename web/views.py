from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings  # <-- IMPORTANTE: Trae las configuraciones del sistema
from .forms import ContactoForm

def home(request):
    return render(request, "web/home.html")

def historia(request):
    return render(request, "web/historia.html")

def mision(request):
    return render(request, "web/mision.html")

def vision(request):
    return render(request, "web/vision.html")

def alumnos(request):
    return render(request, "web/alumnos.html")

def docentes(request):
    return render(request, "web/docentes.html")

def blog(request):
    return render(request, "web/blog.html")


def contacto(request):
    form = ContactoForm()
    
    if request.method == "POST":
        form = ContactoForm(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")
            

            asunto = f"NUEVO MENSAJE DE CONTACTO - CBTa 108"
            cuerpo_correo = f"Has recibido un nuevo mensaje desde el sitio web:\n\nNombre: {nombre}\nCorreo de contacto: {email}\n\nMensaje:\n{mensaje}"
            
            try:
                send_mail(
                    asunto,                               
                    cuerpo_correo,                        
                    settings.DEFAULT_FROM_EMAIL, 
                    ['ing.palacios.omar@gmail.com'],            
                    fail_silently=False,
                )
                return redirect('/contacto/?valido')
            except Exception as e:
                print(f"Error en el servidor de correo: {e}")  
                return redirect('/contacto/?error')

    return render(request, "web/contacto.html", {'form': form})