import random
import time
import matplotlib.pyplot as plt

def simular_big_bang():
    print("\n🚀 Estrategia: Big Bang")
    print("Desplegando toda la nueva versión de una sola vez...")

    time.sleep(1)
    riesgo = random.randint(60, 90)
    tiempo = random.randint(3, 5)
    uptime = random.uniform(70, 95)
    satisfaccion = random.uniform(60, 85)

    print(f"→ Riesgo alto: {riesgo}%")
    print(f"→ Tiempo de despliegue: {tiempo} horas")
    print(f"→ Uptime: {uptime:.2f}%")
    print(f"→ Satisfacción del usuario: {satisfaccion:.2f}%")

    if riesgo > 80:
        print("⚠️ Error crítico detectado, realizando rollback automático...")
        print("Rollback completado. Versión anterior restaurada.\n")

    return {"estrategia": "Big Bang", "riesgo": riesgo, "tiempo": tiempo, "uptime": uptime, "satisfaccion": satisfaccion}


def simular_faseado():
    print("\n⚙️ Estrategia: Faseado")
    print("Desplegando por grupos o módulos de forma progresiva...")

    time.sleep(1)
    riesgo = random.randint(30, 60)
    tiempo = random.randint(5, 8)
    uptime = random.uniform(85, 98)
    satisfaccion = random.uniform(75, 95)

    print(f"→ Riesgo medio: {riesgo}%")
    print(f"→ Tiempo de despliegue: {tiempo} horas")
    print(f"→ Uptime: {uptime:.2f}%")
    print(f"→ Satisfacción del usuario: {satisfaccion:.2f}%\n")

    return {"estrategia": "Faseado", "riesgo": riesgo, "tiempo": tiempo, "uptime": uptime, "satisfaccion": satisfaccion}


def simular_blue_green():
    print("\n🟢 Estrategia: Blue-Green")
    print("Manteniendo dos entornos: Blue (actual) y Green (nuevo)...")

    time.sleep(1)
    riesgo = random.randint(10, 40)
    tiempo = random.randint(2, 4)
    uptime = random.uniform(95, 100)
    satisfaccion = random.uniform(90, 100)

    print(f"→ Riesgo bajo: {riesgo}%")
    print(f"→ Tiempo de despliegue: {tiempo} horas")
    print(f"→ Uptime: {uptime:.2f}%")
    print(f"→ Satisfacción del usuario: {satisfaccion:.2f}%\n")

    return {"estrategia": "Blue-Green", "riesgo": riesgo, "tiempo": tiempo, "uptime": uptime, "satisfaccion": satisfaccion}


def comparar_resultados(resultados):
    print("📊 Comparativo General de Estrategias:\n")
    print(f"{'Estrategia':<12} {'Riesgo':<10} {'Tiempo(h)':<10} {'Uptime(%)':<12} {'Satisfacción(%)'}")
    print("-" * 60)
    for r in resultados:
        print(f"{r['estrategia']:<12} {r['riesgo']:<10} {r['tiempo']:<10} {r['uptime']:<12.2f} {r['satisfaccion']:.2f}")

def graficar_resultados(resultados):
    estrategias = [r["estrategia"] for r in resultados]
    riesgos = [r["riesgo"] for r in resultados]
    tiempos = [r["tiempo"] for r in resultados]
    uptimes = [r["uptime"] for r in resultados]
    satisfacciones = [r["satisfaccion"] for r in resultados]

    # Crear figura y ejes
    plt.figure(figsize=(10, 6))
    plt.suptitle("Comparativo de Estrategias de Despliegue", fontsize=14, fontweight="bold")

    # Subgráfico 1: Riesgo
    plt.subplot(2, 2, 1)
    plt.bar(estrategias, riesgos)
    plt.title("Nivel de Riesgo (%)")
    plt.ylabel("%")

    # Subgráfico 2: Tiempo
    plt.subplot(2, 2, 2)
    plt.bar(estrategias, tiempos, color="orange")
    plt.title("Tiempo de Despliegue (h)")
    plt.ylabel("Horas")

    # Subgráfico 3: Uptime
    plt.subplot(2, 2, 3)
    plt.bar(estrategias, uptimes, color="green")
    plt.title("Uptime (%)")
    plt.ylabel("%")

    # Subgráfico 4: Satisfacción
    plt.subplot(2, 2, 4)
    plt.bar(estrategias, satisfacciones, color="purple")
    plt.title("Satisfacción del Usuario (%)")
    plt.ylabel("%")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()