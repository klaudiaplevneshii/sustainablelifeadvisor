from .utils import estimate_footprint
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def hola(request):
    return HttpResponse("¡Hola Django!")

def calculate(request):
    resultado = None

    if request.method == 'POST':

        transport = request.POST.get('transport')
        passenger = 1
        distance = float(request.POST.get('distance', 0))
        energy = float(request.POST.get('energy', 0))
        gas = float(request.POST.get('gas', 0))
        fuel = request.POST.get('fuel')
        litros = float(request.POST.get('litros', 0))

        result = estimate_footprint(
            transport,
            passenger,
            distance,
            energy,
            gas,
            fuel,
            litros
        )

        context = {
                'result': result,                 
        }
    else:
        context = {'result': None}

    template = loader.get_template('form.html')
    return HttpResponse(template.render(context, request))