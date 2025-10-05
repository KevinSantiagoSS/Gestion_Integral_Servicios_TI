import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# --- Configuración general ---
st.set_page_config(page_title="Dashboard TI", layout="wide")

st.title("📊 Dashboard Estratégico de TI")
st.markdown("Visualización de métricas de soporte, desempeño y capacidad predictiva")

# --- Generar datos simulados ---
dias = pd.date_range(datetime.now() - timedelta(days=10), datetime.now(), freq="D")
datos = {
    "Fecha": dias,
    "Tickets_Resueltos": [random.randint(5, 15) for _ in dias],
    "SLA_Cumplimiento": [random.uniform(80, 100) for _ in dias],
    "Satisfaccion": [random.uniform(70, 100) for _ in dias],
    "Capacidad_Usada": [random.uniform(50, 95) for _ in dias]
}
df = pd.DataFrame(datos)

# --- Vistas del Dashboard ---
opcion = st.sidebar.selectbox("Selecciona vista", ["Ejecutiva", "Operativa", "Predictiva"])

if opcion == "Ejecutiva":
    st.subheader("🧭 Vista Ejecutiva")
    col1, col2, col3 = st.columns(3)
    col1.metric("Cumplimiento SLA", f"{df['SLA_Cumplimiento'].iloc[-1]:.1f}%")
    col2.metric("Satisfacción Usuario", f"{df['Satisfaccion'].iloc[-1]:.1f}%")
    col3.metric("Tickets resueltos hoy", df['Tickets_Resueltos'].iloc[-1])

    fig, ax = plt.subplots()
    ax.plot(df["Fecha"], df["SLA_Cumplimiento"], label="SLA (%)", marker="o")
    ax.plot(df["Fecha"], df["Satisfaccion"], label="Satisfacción (%)", marker="s")
    ax.legend()
    ax.set_title("Evolución SLA y Satisfacción")
    st.pyplot(fig)

elif opcion == "Operativa":
    st.subheader("⚙️ Vista Operativa")
    st.bar_chart(df[["Tickets_Resueltos", "Capacidad_Usada"]])

    st.write("Promedio diario de tickets resueltos:",
             round(df["Tickets_Resueltos"].mean(), 2))

    st.write("Capacidad promedio usada:",
             f"{df['Capacidad_Usada'].mean():.2f}%")

elif opcion == "Predictiva":
    st.subheader("📈 Vista Predictiva")
    # Proyección sencilla: tendencia lineal basada en promedio
    df_pred = df.copy()
    tendencia = df["Tickets_Resueltos"].rolling(window=3).mean()
    fig, ax = plt.subplots()
    ax.plot(df["Fecha"], df["Tickets_Resueltos"], label="Histórico")
    ax.plot(df["Fecha"], tendencia, label="Tendencia (3 días)", linestyle="--")
    ax.set_title("Proyección de tickets resueltos")
    ax.legend()
    st.pyplot(fig)

    st.write("Basado en la tendencia, se espera mantener el nivel de respuesta o mejorarlo en los próximos días.")
