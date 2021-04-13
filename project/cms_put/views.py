
from django.http import HttpResponse
from .models import Contenido
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_content(request, llave):
    if request.method == "PUT":
        valor = request.body.decode('utf-8')
        content = Contenido(clave=llave, valor=valor)
        content.save()

    try:
        respuesta = Contenido.objects.get(clave=llave).valor
    except Contenido.DoesNotExist:
        respuesta = 'No existe contenido para la clave ' + llave
    return HttpResponse(respuesta)
