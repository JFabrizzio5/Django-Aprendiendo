from django.http import HttpResponse 
from django.shortcuts import render
from django.template import loader
from django.template import Template,Context
import os

def saludo(request):
    template = loader.get_template("template.html")
    mensaje = "¡Hola, bienvenido a Django!"
    return HttpResponse(template.render())
def steam2(request, mensaje=None):  # Parámetro 'mensaje' con valor predeterminado None
    # Si el mensaje no se proporciona en la URL, utiliza un valor predeterminado
    if mensaje is None:
        mensaje = "¡Hola, mundo predeterminado!"

    # Obtén la ruta al directorio del proyecto
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Construye la ruta al archivo HTML utilizando BASE_DIR
    ruta_al_archivo = os.path.join(BASE_DIR, "nombre_del_proyecto/templates/template.html")
    
    # Abre y lee el archivo HTML
    with open(ruta_al_archivo, 'r') as archivo:
        contenido_html = archivo.read()

    # Crea un objeto Template y renderiza el contenido con el mensaje (predeterminado o proporcionado)
    plt = Template(contenido_html)
    ctx = Context({'mensaje': mensaje})  # Agrega el mensaje al contexto
    docexterno = plt.render(ctx)

    return HttpResponse(docexterno)