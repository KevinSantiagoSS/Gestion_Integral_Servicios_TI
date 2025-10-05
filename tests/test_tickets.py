from modules.tickets import asignar_prioridad

def test_prioridades():
    assert asignar_prioridad("El servidor está caído") == "Crítico"
    assert asignar_prioridad("El PC no funciona") == "Alto"
    assert asignar_prioridad("El sistema está lento") == "Medio"
    assert asignar_prioridad("Consulta general") == "Bajo"

print("✅ Pruebas de prioridad pasadas correctamente.")
