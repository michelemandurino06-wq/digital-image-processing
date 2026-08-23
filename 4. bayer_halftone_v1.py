# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np

def apply_bayer_halftone(image_path, output_path):
    # 1. Caricamento immagine e conversione in scala di grigi ('L')
    img = Image.open(image_path).convert('L')
    pixels = np.array(img, dtype=float)
    height, width = pixels.shape

    # 2. Definizione della Matrice di Bayer 4x4
    # I valori sono normalizzati tra 0 e 255
    bayer_matrix = np.array([
        [ 0, 128,  32, 160],
        [192,  64, 224,  96],
        [ 48, 176,  16, 144],
        [240, 112, 208,  80]
    ])

    # 3. Creazione dell'immagine di output
    output = np.zeros((height, width), dtype=np.uint8)

    # 4. Processo di Dithering
    for y in range(height):
        for x in range(width):
            # Troviamo la soglia corrispondente nella matrice di Bayer
            # Usiamo l'operatore modulo (%) per ripetere la matrice su tutta l'immagine
            threshold = bayer_matrix[y % 4, x % 4]
            
            # Trasformazione in Bianco o Nero
            if pixels[y, x] > threshold:
                output[y, x] = 255
            else:
                output[y, x] = 0

    # 5. Salvataggio e visualizzazione
    result_img = Image.fromarray(output)
    result_img.save(output_path)
    result_img.show()
    print(f"Immagine salvata con successo in: {output_path}")

# --- CONFIGURAZIONE ---
# Incolla qui il percorso della tua immagine
input_file = "C:/Users/rober/OneDrive/Desktop/corridoio_scuro.jpg"
output_file = "risultato_halftone.png"

apply_bayer_halftone(input_file, output_file)
