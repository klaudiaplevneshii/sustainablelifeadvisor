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
