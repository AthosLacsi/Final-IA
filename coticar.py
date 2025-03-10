import streamlit as st
import groq
import json

# Configura tu API Key
API_KEY = "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" 

# Inicializa el cliente de Groq
client = groq.Client(api_key=API_KEY)

def obtener_cotizacion_dolar():
    """Solicita al usuario la cotización del dólar blue en pesos argentinos"""
    dolar_blue = st.number_input("Ingrese la cotización actual del dólar blue (en ARS): ", min_value=0.01)
    return dolar_blue

def calcular_costos(vehiculo_usd, dolar_blue):
    """Calcula los costos mensuales del vehículo en ARS"""
    vehiculo_ars = vehiculo_usd * dolar_blue

    # Estimaciones de costos mensuales (pueden ajustarse según el modelo del vehículo)
    seguro = vehiculo_ars * 0.01  # 1% del valor del auto
    patente = vehiculo_ars * 0.015 / 12  # 1.5% anual dividido en 12 meses
    combustible = 50000  # Estimación mensual en ARS
    mantenimiento = 30000  # Estimación mensual en ARS
    total_mensual = seguro + patente + combustible + mantenimiento

    return {
        "Precio en ARS": vehiculo_ars,
        "Seguro": seguro,
        "Patente": patente,
        "Combustible": combustible,
        "Mantenimiento": mantenimiento,
        "Total mensual": total_mensual
    }

def generar_respuesta_ia(costos):
    """Usa IA para generar una respuesta más detallada basada en los costos calculados"""
    prompt = f"""
    Un usuario quiere comprar un auto y desea conocer sus costos mensuales en Argentina. 
    Basado en estos datos:

    - Precio en ARS: {costos["Precio en ARS"]:.2f}
    - Seguro mensual: {costos["Seguro"]:.2f}
    - Patente mensual: {costos["Patente"]:.2f}
    - Combustible mensual: {costos["Combustible"]:.2f}
    - Mantenimiento mensual: {costos["Mantenimiento"]:.2f}
    - Costo total mensual estimado: {costos["Total mensual"]:.2f}

    Genera un análisis financiero claro y aconseja al usuario sobre si esta compra es viable.
    """

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500  # Aumentado el límite de tokens
    )

    return response.choices[0].message.content.strip()

# Interfaz de usuario con Streamlit
st.title("Calculadora de Costos de Vehículos en Argentina")
vehiculo_usd = st.number_input("Ingrese el precio del vehículo en dólares: ", min_value=0.01)

# Solicitar sueldo
sueldo = st.number_input("Ingrese su sueldo mensual en ARS: ", min_value=0.01)

if vehiculo_usd > 0 and sueldo > 0:
    dolar_blue = obtener_cotizacion_dolar()
    if dolar_blue > 0:
        costos = calcular_costos(vehiculo_usd, dolar_blue)
        st.subheader("Estimación de costos mensuales:")
        for clave, valor in costos.items():
            st.write(f"{clave}: ${valor:,.2f} ARS")

        # Análisis de viabilidad basado en el sueldo
        if costos["Total mensual"] > sueldo:
            st.subheader("Análisis de viabilidad:")
            st.write(f"¡El costo mensual del vehículo (${costos['Total mensual']:,.2f} ARS) es mayor que tu sueldo (${sueldo:,.2f} ARS)! No parece ser una compra viable.")
        else:
            st.subheader("Análisis de viabilidad:")
            st.write(f"El costo mensual del vehículo (${costos['Total mensual']:,.2f} ARS) es menor que tu sueldo (${sueldo:,.2f} ARS), lo que hace que la compra sea más viable.")

        # Análisis de IA
        st.subheader("Análisis detallado de IA:")
        st.write(generar_respuesta_ia(costos))
