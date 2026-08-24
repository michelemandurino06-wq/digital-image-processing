# -*- coding: utf-8 -*-"""
import numpy as np
from PIL import Image
import os

def equalize_histogram(image_path):
    # 1. Automatic path cleanup (removes quotes and extra spaces)
    clean_path = image_path.strip().replace('"', '').replace("'", "")
    
    if not os.path.exists(clean_path):
        raise FileNotFoundError(f"File not found: {clean_path}")

    # 2. Image processing
    img = Image.open(clean_path).convert('L')
    img_array = np.array(img)

    histogram, _ = np.histogram(img_array.flatten(), bins=256, range=[0, 256])
    cdf = histogram.cumsum()

    cdf_mask = np.ma.masked_equal(cdf, 0)
    cdf_mask = (cdf_mask - cdf_mask.min()) * 255 / (cdf_mask.max() - cdf_mask.min())
    cdf_final = np.ma.filled(cdf_mask, 0).astype('uint8')

    equalized_img_array = cdf_final[img_array]
    return Image.fromarray(equalized_img_array)

# --- PASTE PATH BELOW ---
test_image_path = r"C:..."

try:
    result = equalize_histogram(test_image_path)
    result.show()
    print("Success! Immagine processed successfully.")
except Exception as e:
    print(f"ERRORE: {e}")
