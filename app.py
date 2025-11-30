import streamlit as st
from credit_decision import evaluar_credito

st.title("🏦 Gestor de Decisión de Crédito")
st.write("Complete los siguientes datos para evaluar su solicitud de crédito.")

# Entradas del usuario
edad = st.number_input("Edad", min_value=18, max_value=100, value=30)
ingresos_mensuales = st.number_input("Ingresos mensuales (€)", min_value=0, value=2500)
deuda_actual = st.number_input("Deuda actual (€)", min_value=0, value=500)
historial_crediticio = st.selectbox("Historial crediticio", ["bueno", "regular", "malo"])
empleo_estable = st.checkbox("¿Tiene empleo estable?")
monto_solicitado = st.number_input("Monto solicitado (€)", min_value=0, value=10000)

# Botón de evaluación
if st.button("Evaluar solicitud"):
    aprobado = evaluar_credito(
        edad=edad,
        ingresos_mensuales=ingresos_mensuales,
        deuda_actual=deuda_actual,
        historial_crediticio=historial_crediticio,
        empleo_estable=empleo_estable,
        monto_solicitado=monto_solicitado
    )
    
    if aprobado:
        st.success("✅ ¡Su crédito ha sido APROBADO!")
    else:
        st.error("❌ Su crédito ha sido RECHAZADO.")