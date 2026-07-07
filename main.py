import json
import os

def validar_cedula(cedula: str) -> bool:
    """Valida que la cédula tenga 10 dígitos y sea numérica."""
    return cedula.isdigit() and len(cedula) == 10

def registrar_tramite(nombre: str, cedula: str, tipo_tramite: str):
    """Guarda el trámite en un archivo JSON."""
    if not validar_cedula(cedula):
        raise ValueError("Cédula inválida")
    
    # Crear carpeta data si no existe
    if not os.path.exists('data'):
        os.makedirs('data')
        
    datos = {"nombre": nombre, "cedula": cedula, "tipo_tramite": tipo_tramite}
    
    with open("data/tramites.json", "a", encoding="utf-8") as f:
        json.dump(datos, f)
        f.write("\n")
    return True