import requests

def estimate_footprint(
    transport, passenger, Distance_km,
    energia_kwh, gas_m3,
    tipo_combustible, litros_combustible
):
    # Public transport
    emissions_transport = 0
    if transport == 'bus':
        emissions_transport = 0.105 * Distance_km * passenger
    elif transport == 'train':
        emissions_transport = 0.041 * Distance_km * passenger
    elif transport == 'bike':
        emissions_transport = 0
    elif transport == 'car':
        # supondremos 0.192 kg CO₂/km por defecto por auto particular
        emissions_transport = 0.192 * Distance_km

    # Electricidad
    emissions_energia = energia_kwh * 0.233

    # Gas natural
    emissions_gas = gas_m3 * 2.0

    # Combustible particular
    if tipo_combustible == 'petrol':
        emissions_auto = litros_combustible * 2.31
    elif tipo_combustible == 'diesel':
        emissions_auto = litros_combustible * 2.68
    else:
        emissions_auto = 0

    # Total
    total = emissions_transport + emissions_energia + emissions_gas + emissions_auto
    return round(total, 2)


# Tabla de emisiones de CO₂ por fuente de energía y transport
#| Fuente           | Emisión estimada           |
#| ---------------- | -------------------------- |
#| 🚗 Auto (petrol) | 2.31 kg CO₂ / litro        |
#| 🚙 Auto (diesel) | 2.68 kg CO₂ / litro        |
#| 🚌 Bus           | 0.105 kg CO₂ / pasajero·km |
#| 🚆 Tren          | 0.041 kg CO₂ / pasajero·km |
#| 🚲 Bicicleta     | 0 kg CO₂                   |
#| ⚡ Electricidad  | 0.233 kg CO₂ / kWh         |
#| 🔥 Gas natural   | 2.0 kg CO₂ / m³            |

# ---------------------------------------------
# 🌿 AI Suggestion via Mistral API
# ---------------------------------------------

def generate_ai_suggestion_mistral(prompt_text):
    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Authorization": "Bearer w00V1V2iqeNCYiCYPiofaE2HL0pRYrQM",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-medium",
        "messages": [
            {"role": "user", "content": prompt_text}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return f"[ERROR] {response.status_code}: {response.text}"