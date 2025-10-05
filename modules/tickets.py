import sqlite3
from datetime import datetime

DB_PATH = "data/tickets.db"

# Inicializa la BD si no existe
def inicializar_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        problema TEXT,
        categoria TEXT,
        prioridad TEXT,
        estado TEXT DEFAULT 'Abierto',
        fecha TEXT
    )
    """)
    conn.commit()
    conn.close()

def asignar_prioridad(problema):
    problema = problema.lower()
    if "caída" in problema or "servidor" in problema:
        return "Crítico"
    elif "error" in problema or "no funciona" in problema:
        return "Alto"
    elif "lento" in problema:
        return "Medio"
    else:
        return "Bajo"

def crear_ticket(usuario, problema, categoria):
    inicializar_db()
    prioridad = asignar_prioridad(problema)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tickets (usuario, problema, categoria, prioridad, fecha) VALUES (?, ?, ?, ?, ?)",
                   (usuario, problema, categoria, prioridad, fecha))
    conn.commit()
    conn.close()

    print(f"✅ Ticket creado con prioridad {prioridad}")

def mostrar_tickets():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, usuario, problema, prioridad, estado, fecha FROM tickets")
    registros = cursor.fetchall()
    conn.close()

    if not registros:
        print("⚠️ No hay tickets registrados.")
    else:
        print("\n--- LISTA DE TICKETS ---")
        for t in registros:
            print(f"[{t[0]}] {t[1]} - {t[2]} | Prioridad: {t[3]} | Estado: {t[4]} | Fecha: {t[5]}")
