# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:30:29 2026

@author: rober
"""

import numpy as np
from PIL import Image
import os

def equalizza_istogramma(percorso_immagine):
    # 1. Pulizia automatica del percorso (toglie virgolette e spazi extra)
    percorso_pulito = percorso_immagine.strip().replace('"', '').replace("'", "")
    
    if not os.path.exists(percorso_pulito):
        raise FileNotFoundError(f"Il file non è stato trovato qui: {percorso_pulito}")

    # 2. Elaborazione immagine
    img = Image.open(percorso_pulito).convert('L')
    img_array = np.array(img)

    istogramma, _ = np.histogram(img_array.flatten(), bins=256, range=[0, 256])
    cdf = istogramma.cumsum()

    cdf_mask = np.ma.masked_equal(cdf, 0)
    cdf_mask = (cdf_mask - cdf_mask.min()) * 255 / (cdf_mask.max() - cdf_mask.min())
    cdf_final = np.ma.filled(cdf_mask, 0).astype('uint8')

    img_equalizzata_array = cdf_final[img_array]
    return Image.fromarray(img_equalizzata_array)

# --- INCOLLA QUI SOTTO ---
# Premi tasto destro sul file -> "Copia come percorso" -> Incolla tra le virgolette
percorso_da_testare = r"C:\Users\rober\OneDrive\Desktop\corridoio_scuro.jpg"

try:
    risultato = equalizza_istogramma(percorso_da_testare)
    risultato.show()
    print("Successo! Immagine elaborata correttamente.")
except Exception as e:
    print(f"ERRORE: {e}")
