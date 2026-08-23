# -*- coding: utf-8 -*-
from PIL import Image

# 1. CHIEDI IL PERCORSO (Incolla qui il percorso della tua immagine)
percorso = input("Trascina qui l'immagine o scrivi il percorso: ").strip().replace('"', '')

# 2. APRI E TRASFORMA IN LISTA DI NUMERI
img = Image.open(percorso).convert('L')
pixel_originali = list(img.getdata())

# 3. COMPRESSIONE RLE (Logica base)
dati_compressi = []
if pixel_originali:
    pixel_precedente = pixel_originali[0]
    contatore = 0
    
    for pixel in pixel_originali:
        if pixel == pixel_precedente:
            contatore += 1
        else:
            dati_compressi.append((contatore, pixel_precedente))
            pixel_precedente = pixel
            contatore = 1
    
    # Salva l'ultimo gruppo
    dati_compressi.append((contatore, pixel_precedente))

# 4. MOSTRA IL RISULTATO
print(f"\nPixel originali: {len(pixel_originali)}")
print(f"Coppie RLE create: {len(dati_compressi)}")

# Esempio visivo di cosa è successo:
print(f"\nPrimi 5 gruppi (Conteggio, Colore): {dati_compressi[:5]}")
