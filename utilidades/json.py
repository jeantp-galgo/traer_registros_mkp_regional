import json

class utilidad_json:

    def guardar(nombre_archivo, datos):
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        print(f"El archivo '{nombre_archivo}' ha sido creado con la información en formato JSON.")

    def leer(ruta_json):
        with open(ruta_json, 'r', encoding='utf-8') as file:
            # Carga el contenido del archivo en un diccionario
            data = json.load(file)
        return data