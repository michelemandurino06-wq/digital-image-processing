# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
import os

def equalize_rgb(image_path):
    # 1. Clean path and open image
    clean_path = image_path.strip().replace('"', '').replace("'", "")
    if not os.path.exists(clean_path):
        raise FileNotFoundError(f"File not found: {clean_path}")

    img_rgb = Image.open(clean_path).convert('RGB')
    
    # 2. Convert to HSV to isolate luminosity (Value)
    img_hsv = img_rgb.convert('HSV')
    hsv_array = np.array(img_hsv)

    # The V channel (Value/Brightness) is the last one: hsv_array[:, :, 2]
    v_channel = hsv_array[:, :, 2]

    # 3. Compute Histogram and CDF on the V channel only
    histogram, _ = np.histogram(v_channel.flatten(), bins=256, range=[0, 256])
    cdf = histogram.cumsum()

    # 4. CDF Normalization
    cdf_mask = np.ma.masked_equal(cdf, 0)
    cdf_mask = (cdf_mask - cdf_mask.min()) * 255 / (cdf_mask.max() - cdf_mask.min())
    cdf_final = np.ma.filled(cdf_mask, 0).astype('uint8')

    # 5. Apply equalization to the V channel only
    hsv_array[:, :, 2] = cdf_final[v_channel]

    # 6. Convert back to RGB
    equalized_img_hsv = Image.fromarray(hsv_array, mode='HSV')
    return equalized_img_hsv.convert('RGB')

# --- PASTE PATH HERE ---
test_image_path = r"C:..."

try:
    result = equalize_rgb(test_image_path)
    result.show()
    # Optional save
    # result.save("rgb_result.png")
    print("Success! Color contrast optimized.")
except Exception as e:
    print(f"ERRORE: {e}")
