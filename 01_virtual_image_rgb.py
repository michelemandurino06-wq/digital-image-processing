# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 1. Carica l'immagine a colori
img = cv2.imread('...')

# Verifichiamo che l'immagine sia stata caricata correttamente
if img is None:
    print("Errore: Immagine non trovata.")
else:
    # 2. Dividi l'immagine nei tre canali
    # Attenzione: l'ordine in OpenCV è BGR (Blu, Verde, Rosso)
    b, g, r = cv2.split(img)

    # --- OPZIONE 1: Salva i canali come immagini in scala di grigi ---
    # In queste immagini, il bianco rappresenta la massima intensità del canale
    cv2.imwrite('canale_rosso_gray.png', r)
    cv2.imwrite('canale_verde_gray.png', g)
    cv2.imwrite('canale_blu_gray.png', b)

    # --- OPZIONE 2: Salva i canali mantenendo il colore visivo ---
    # Creiamo una matrice di zeri della stessa dimensione di un canale
    zeros = np.zeros_like(b)

    # Uniamo i canali mettendo a zero quelli che non ci servono
    # Formato cv2.merge: [Blu, Verde, Rosso]
    img_rosso = cv2.merge([zeros, zeros, r])
    img_verde = cv2.merge([zeros, g, zeros])
    img_blu   = cv2.merge([b, zeros, zeros])

    # Salva le immagini colorate
    cv2.imwrite('solo_rosso.png', img_rosso)
    cv2.imwrite('solo_verde.png', img_verde)
    cv2.imwrite('solo_blu.png', img_blu)

    print("Elaborazione completata. I file sono stati salvati.")
