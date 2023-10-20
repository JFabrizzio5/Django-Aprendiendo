from django.http import HttpResponse 

def saludo(request):
    mensaje = "¡Hola, bienvenido a Django!"
    return HttpResponse(mensaje)
    
