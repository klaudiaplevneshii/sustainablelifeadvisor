from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.urls import reverse
from .models import EmissionRecord
from .utils import estimate_footprint, generate_ai_suggestion_mistral
import markdown
from django.db.models import Q
from datetime import datetime

def homepage(request):
    return render(request, 'homepage.html')

def about_view(request):
    return render(request, 'about.html')

def impact_view(request):
    return render(request, 'impact.html')

def interpretation_view(request):
    return render(request, 'interpretation.html')

def calculate(request):
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


        record = EmissionRecord.objects.create(
            transport=transport,
            distance=distance,
            energy=energy,
            gas=gas,
            fuel=fuel,
            litres=litros,
            result=result
        )

        return redirect('result_from_db_history', record_id=record.id)

    return render(request, 'form.html')


def view_history(request):
    date_str = request.GET.get('date')
    min_result = request.GET.get('min_result')

    filters = Q()

    if date_str:
        try:
            selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            filters &= Q(created_at__date=selected_date)
        except ValueError:
            selected_date = None
    else:
        selected_date = None

    if min_result:
        filters &= Q(result__gte=float(min_result))

    history = EmissionRecord.objects.filter(filters).order_by('-created_at')

    return render(request, 'history.html', {
        'history': history,
        'selected_date': date_str,
        'selected_min_result': min_result
    })


def clear_history(request):
    if request.method == 'POST':
        EmissionRecord.objects.all().delete()
        return redirect('view_history')

def generate_ai_html_from_inputs(transport, distance, energy, gas, fuel, litros):
    prompt = (
        f"The user drives {distance} km per day using a {transport}, "
        f"uses {energy} kWh of electricity, consumes {gas} m³ of gas, and uses {litros} L of {fuel}. "
        "Suggest 3 practical and friendly ways to reduce their carbon footprint."
    )
    ai_response = generate_ai_suggestion_mistral(prompt)
    html = markdown.markdown(ai_response)
    return html

def result_from_db_history(request, record_id):
    try:
        record = EmissionRecord.objects.get(id=record_id)
    except EmissionRecord.DoesNotExist:
        return redirect('view_history')

    ai_html = generate_ai_html_from_inputs(
        transport=record.transport,
        distance=record.distance,
        energy=record.energy,
        gas=record.gas,
        fuel=record.fuel,
        litros=record.litres
    )

    return render(request, 'result.html', {
        'result': record.result,
        'ai_suggestion_html': mark_safe(ai_html)
    })
