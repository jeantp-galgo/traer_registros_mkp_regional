from google_sheet.utils import *
from utilidades.registros import *
from utilidades.json import *
import pandas as pd
import os
from dotenv import load_dotenv
import sys

load_dotenv()

# Crea una instancia de la clase mongodb_funciones
google_sheet_func = google_sheet_funciones()

def inicio(nombre_hoja):
    print("Leyendo archivo config.json")
    data = utilidad_json.leer(r"./config.json")
    if data:
        print("Archivo leido")
    else:
        print("No hay data")
        return

    hojas = {
        "actualizaciones_mx": ("Solicitudes MX Motos", "MX", "MX Motos"),
        "actualizaciones_cl_autos": ("Solicitudes CL Autos", "CL", "CL Autos"),
        "actualizaciones_cl_motos": ("Solicitudes CL Motos", "CL", "CL Motos"),
        "actualizaciones_co_motos": ("Solicitudes CO Motos", "CO", "CO Motos"),
        "actualizaciones_pe_motos": ("Solicitudes PE Motos", "PE", "PE Motos")
    }

    print(f"La hoja elegida es: {nombre_hoja}")
    if nombre_hoja in hojas:
        nombre_hoja_google, pais, tipo_vehiculo = hojas[nombre_hoja]
        datos = google_sheet_func.leer_datos_google_sheet(data["nombre_archivo"], nombre_hoja_google)
        df = pd.DataFrame(datos)
        if nombre_hoja == "actualizaciones_cl_autos":
            crear_registros_json_auto(df, pais, nombre_hoja)
        else:
            crear_registros_json(df, pais, nombre_hoja)
    else:
        print("Nombre de hoja no válido.")
        print("Hojas disponibles: actualizaciones_mx, actualizaciones_cl_autos, actualizaciones_cl_motos, actualizaciones_co_motos, actualizaciones_pe_motos")
        return

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Uso: py inicio.py 'nombre_hoja' ")
        print("Hojas disponibles: actualizaciones_mx, actualizaciones_cl_autos, actualizaciones_cl_motos, actualizaciones_co_motos, actualizaciones_pe_motos")
        sys.exit(1)

    nombre_hoja = sys.argv[1]

    # Llama a la función inicio con el nombre de vehículo opcional
    inicio(nombre_hoja)





























