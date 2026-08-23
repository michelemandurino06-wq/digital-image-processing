# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:33:20 2026

@author: rober
"""

import numpy as np
from PIL import Image
import os

def equalizza_rgb(percorso_immagine):
    # 1. Pulizia percorso e apertura immagine
    percorso_pulito = percorso_immagine.strip().replace('"', '').replace("'", "")
    if not os.path.exists(percorso_pulito):
        raise FileNotFoundError(f"File non trovato: {percorso_pulito}")

    img_rgb = Image.open(percorso_pulito).convert('RGB')
    
    # 2. Convertiamo in HSV per isolare la luminosità (Value)
    img_hsv = img_rgb.convert('HSV')
    hsv_array = np.array(img_hsv)

    # Il canale V (Value/Luminosità) è l'ultimo: hsv_array[:, :, 2]
    v_channel = hsv_array[:, :, 2]

    # 3. Calcolo Istogramma e CDF solo sul canale V
    istogramma, _ = np.histogram(v_channel.flatten(), bins=256, range=[0, 256])
    cdf = istogramma.cumsum()

    # 4. Normalizzazione della CDF
    cdf_mask = np.ma.masked_equal(cdf, 0)
    cdf_mask = (cdf_mask - cdf_mask.min()) * 255 / (cdf_mask.max() - cdf_mask.min())
    cdf_final = np.ma.filled(cdf_mask, 0).astype('uint8')

    # 5. Applichiamo l'equalizzazione solo al canale V
    hsv_array[:, :, 2] = cdf_final[v_channel]

    # 6. Riconversione in RGB
    img_equalizzata_hsv = Image.fromarray(hsv_array, mode='HSV')
    return img_equalizzata_hsv.convert('RGB')

# --- INCOLLA QUI IL PERCORSO ---
percorso_da_testare = r"C:\Users\rober\OneDrive\Desktop\castello.jpg"

try:
    risultato = equalizza_rgb(percorso_da_testare)
    risultato.show()
    # Salvataggio facoltativo
    # risultato.save("risultato_rgb.png")
    print("Successo! Contrasto colore ottimizzato.")
except Exception as e:
    print(f"ERRORE: {e}")
