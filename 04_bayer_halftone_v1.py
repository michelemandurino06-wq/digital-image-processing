# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np

def apply_bayer_halftone(image_path, output_path):
    # 1. Load image and convert to grayscale ('L')
    img = Image.open(image_path).convert('L')
    pixels = np.array(img, dtype=float)
    height, width = pixels.shape

    # 2. Define the 4x4 Bayer Matrix
    # Values are normalized between 0 and 255
    bayer_matrix = np.array([
        [ 0, 128,  32, 160],
        [192,  64, 224,  96],
        [ 48, 176,  16, 144],
        [240, 112, 208,  80]
    ])

    # 3. Create the output image array
    output = np.zeros((height, width), dtype=np.uint8)

    # 4. Dithering process
    for y in range(height):
        for x in range(width):
            # Find corresponding  threshold in the Bayer martrix
            # Use modulo operator (%) to title the matrix across the image
            threshold = bayer_matrix[y % 4, x % 4]
            
            # Convert to Black or White
            if pixels[y, x] > threshold:
                output[y, x] = 255
            else:
                output[y, x] = 0

    # 5. Save and display
    result_img = Image.fromarray(output)
    result_img.save(output_path)
    result_img.show()
    print(f"Image successfully saved to: {output_path}")

# --- CONFIGURATION ---
# Paste your image path here
input_file = "C:..."
output_file = "halftone_result.png"

apply_bayer_halftone(input_file, output_file)
