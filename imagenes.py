from PIL import Image
import os

# 1. Definir los archivos y las listas de nombres asociados a cada imagen
imagenes_a_procesar = [
    {
        "archivo": "Gemini_Generated_Image_w46sebw46sebw46s.jpg",
        "nombres": [
            "Napolitana_york_queso", "Panini", "Empanadilla_grande", "Empanadilla_pequena", "Trenza_choco_grande", "Trenza_nueces_pecan",
            "Espartero", "Cana_de_chocolate", "Mona_de_pascua", "Limon", "Lata_refresco", "Red_Bull",
            "Agua_con_gas", "Agua_pequena", "Agua_grande", "Zumo", "Schweppes", "Nestea",
            "Aquarius", "Radler", "Alhambra_reserva", "San_Miguel_selecta", "Mahou_00_tostada", "Croissant"
        ]
    },
    {
        "archivo": "Gemini_Generated_Image_cz22wcz22wcz22wc.jpg",
        "nombres": [
            "Zumo_vaso", "Papas", "Olivas", "Kinder", "Cacahuetes", "Velas_cumpleanos",
            "Bolsa_plastico", "Donut_chocolate", "Copa_vino_tinto", "Copa_vino_blanco", "Copa_vino_gaseosa", "Bolsa_hielo",
            "Botella_leche", "Plato_pasta", "Sandwich_mixto", "Te", "Terry", "JB",
            "Pacharan", "Ballantines", "Cutty_Sark", "Cazalla", "Ron", "Baileys"
        ]
    }
]

# 2. Configurar la matriz y la carpeta de destino
columnas = 6
filas = 4
carpeta_salida = "imagenes_tpv_completas"
os.makedirs(carpeta_salida, exist_ok=True)

# 3. Procesar cada imagen en bucle
for item in imagenes_a_procesar:
    imagen_path = item["archivo"]
    nombres_productos = item["nombres"]
    
    try:
        img = Image.open(imagen_path)
    except FileNotFoundError:
        print(f"Error: No se encontró la imagen {imagen_path}. Saltando al siguiente archivo.")
        continue

    ancho, alto = img.size
    ancho_celda = ancho // columnas
    alto_celda = alto // filas

    indice = 0
    print(f"\nProcesando {imagen_path}...")
    
    for fila in range(filas):
        for col in range(columnas):
            if indice >= len(nombres_productos):
                break
                
            # Calcular las coordenadas exactas del recorte
            izq = col * ancho_celda
            arr = fila * alto_celda
            der = izq + ancho_celda
            aba = arr + alto_celda
            
            # Recortar y guardar
            recorte = img.crop((izq, arr, der, aba))
            nombre_archivo = os.path.join(carpeta_salida, f"{nombres_productos[indice]}.jpg")
            recorte.save(nombre_archivo, quality=95)
            print(f"  -> Guardado: {nombre_archivo}")
            
            indice += 1

print(f"\n¡Listo! Tienes las 48 imágenes preparadas para el TPV en la carpeta '{carpeta_salida}'.")