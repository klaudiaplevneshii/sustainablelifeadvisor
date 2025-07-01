from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.utils.safestring import mark_safe
import markdown
from django.shortcuts import redirect
from .models import EmissionRecord

from .utils import estimate_footprint, generate_ai_suggestion_mistral

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

        entry = {
            'transport': transport,
            'distance': distance,
            'energy': energy,
            'gas': gas,
            'fuel': fuel,
            'litres': litros,
            'result': result
        }

        history = request.session.get('user_history', [])
        history.append(entry)
        request.session['user_history'] = history

        prompt = (
            f"The user drives {distance} km per day using a {transport}, "
            f"uses {energy} kWh of electricity, consumes {gas} m³ of gas, and uses {litros} L of {fuel}. "
            "Suggest 3 practical and friendly ways to reduce their carbon footprint."
        )

        ai_response = generate_ai_suggestion_mistral(prompt)
        html = markdown.markdown(ai_response)

        context = {
            'result': result,
            'ai_suggestion_html': mark_safe(html)
        }

    else:
        context = {
            'result': None,
            'ai_suggestion': None
        }

    template = loader.get_template('form.html')
    return HttpResponse(template.render(context, request))


def about_view(request):
    return render(request, 'about.html')

def homepage(request):
    return render(request, 'homepage.html')

def view_history(request):
    history = request.session.get('user_history', [])
    return render(request, 'history.html', {'history': history})


def clear_history(request):
    if request.method == 'POST':
        request.session['user_history'] = []
        return redirect('view_history')


def impact_view(request):
    return render(request, 'impact.html')
