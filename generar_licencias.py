import json
import uuid
from datetime import datetime, timedelta

ARCHIVO_LICENCIAS = "licencias.json"

def cargar_licencias():
    try:
        with open(ARCHIVO_LICENCIAS, "r") as f:
            return json.load(f)
    except:
        return {}

def guardar_licencias(data):
    with open(ARCHIVO_LICENCIAS, "w") as f:
        json.dump(data, f, indent=4)

def generar_licencia(dias=30):
    licencias = cargar_licencias()

    nueva_licencia = str(uuid.uuid4()).upper()

    fecha_inicio = datetime.now()
    fecha_expiracion = fecha_inicio + timedelta(days=dias)

    licencias[nueva_licencia] = {
        "activa": True,
        "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d %H:%M:%S"),
        "fecha_expiracion": fecha_expiracion.strftime("%Y-%m-%d %H:%M:%S")
    }

    guardar_licencias(licencias)

    print("\n===================================")
    print("LICENCIA GENERADA CORRECTAMENTE")
    print("===================================")
    print(f"LICENCIA: {nueva_licencia}")
    print(f"EXPIRA: {fecha_expiracion}")
    print("===================================\n")

if __name__ == "__main__":
    generar_licencia()
