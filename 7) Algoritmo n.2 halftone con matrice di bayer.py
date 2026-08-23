# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:58:24 2026

@author: rober
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def process_and_plot(image_path):
    # 1. Caricamento e conversione in grigio
    img_orig = Image.open(image_path).convert('L')
    pixels_orig = np.array(img_orig)
    
    # 2. Definizione Matrice di Bayer 4x4 (Normalizzata)
    bayer_indices = np.array([
        [ 0, 12,  3, 15],
        [12,  4, 14,  6],
        [ 3, 15,  1, 13],
        [15,  7, 13,  5]
    ])
    # Convertiamo gli indici in soglie 0-255
    bayer_matrix = ((bayer_indices + 0.5) / 16 * 255).astype(float)

    # 3. Applicazione Dithering
    h, w = pixels_orig.shape
    pixels_halftone = np.zeros((h, w), dtype=np.uint8)
    
    for y in range(h):
        for x in range(w):
            threshold = bayer_matrix[y % 4, x % 4]
            pixels_halftone[y, x] = 255 if pixels_orig[y, x] > threshold else 0

    # 4. Creazione del Plot (Griglia 2x2)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Confronto Halftone: Matrice di Bayer', fontsize=16)

    # --- Riga 1: Immagini ---
    axs[0, 0].imshow(pixels_orig, cmap='gray')
    axs[0, 0].set_title("Originale (Scala di Grigio)")
    axs[0, 0].axis('off')

    axs[0, 1].imshow(pixels_halftone, cmap='gray')
    axs[0, 1].set_title("Halftone (Bayer 4x4)")
    axs[0, 1].axis('off')

    # --- Riga 2: Istogrammi ---
    # Istogramma Originale
    axs[1, 0].hist(pixels_orig.ravel(), bins=256, color='gray', range=(0, 256))
    axs[1, 0].set_title("Istogramma Originale")
    axs[1, 0].set_xlabel("Intensità Pixel")
    axs[1, 0].set_ylabel("Frequenza")

    # Istogramma Halftone
    axs[1, 1].hist(pixels_halftone.ravel(), bins=256, color='black', range=(0, 256))
    axs[1, 1].set_title("Istogramma Halftone (Binario)")
    axs[1, 1].set_xlabel("Intensità Pixel")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Incolla qui il tuo percorso
process_and_plot("C:/Users/rober/OneDrive/Desktop/corridoio_scuro.jpg")