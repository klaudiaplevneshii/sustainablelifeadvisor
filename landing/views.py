from .utils import estimate_footprint
from django.template import loader
from .utils import estimate_footprint, generate_ai_suggestion_mistral
from django.utils.safestring import mark_safe

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("¡Hello Django!")

def calculate(request):
    result = None

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

        prompt = (
            f"The user drives {distance} km per day using a {transport}, "
            f"uses {energy} kWh of electricity, consumes {gas} m³ of gas, and uses {litros} L of {fuel}. "
            "Suggest 3 practical and friendly ways to reduce their carbon footprint."
        )

        ai_response = generate_ai_suggestion_mistral(prompt)

        context = {
            'result': result,
            'ai_suggestion_html': mark_safe(ai_response.replace('\n', '<br>'))
        }
    else:
        context = {
            'result': None,
            'ai_suggestion': None
        }

    template = loader.get_template('form.html')
    return HttpResponse(template.render(context, request))

from django.shortcuts import render

def about_view(request):
    return render(request, 'about.html')

def homepage(request):
    return render(request, 'homepage.html')

