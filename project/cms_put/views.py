
from django.http import HttpResponse
from .models import Contenido
from django.views.decorators.csrf import csrf_exempt

formulario = """
No existe valor en la base de datos para esta llave.
<p>Introdúcela:
<p>
<form action="" method="POST">
    Valor: <input type="text" name="valor">
    <br/><input type="submit" value="Submit">
</form>
"""
@csrf_exempt
def get_content(request, llave):

    if request.method == "POST":
        valor = request.POST['valor']
        content = Contenido(clave=llave, valor=valor)
        content.save()

    if request.method == "PUT":
        valor = request.body.decode('utf-8')
        content = Contenido(clave=llave, valor=valor)
        content.save()

    try:
        respuesta = Contenido.objects.get(clave=llave).valor
    except Contenido.DoesNotExist:
        respuesta = 'No existe contenido para la clave ' + llave + '\n' + formulario
    except Contenido.MultipleObjectsReturned:
        respuesta = Contenido.objects.filter(clave=llave).last().valor

    return HttpResponse(respuesta)
