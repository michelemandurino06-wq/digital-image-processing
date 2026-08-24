# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def process_and_plot(image_path):
    # 1. Load image and convert to grayscale
    img_orig = Image.open(image_path).convert('L')
    pixels_orig = np.array(img_orig)
    
    # 2. Define the 4x4 Bayer Matrix (Normalized)
    bayer_indices = np.array([
        [ 0, 12,  3, 15],
        [12,  4, 14,  6],
        [ 3, 15,  1, 13],
        [15,  7, 13,  5]
    ])
    # Convert indices to thresholds in range 0-255
    bayer_matrix = ((bayer_indices + 0.5) / 16 * 255).astype(float)

    # 3. Apply Dithering
    h, w = pixels_orig.shape
    pixels_halftone = np.zeros((h, w), dtype=np.uint8)
    
    for y in range(h):
        for x in range(w):
            threshold = bayer_matrix[y % 4, x % 4]
            pixels_halftone[y, x] = 255 if pixels_orig[y, x] > threshold else 0

    # 4. Create Plot (2x2 Grid)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Halftone Comparison: Bayer Matrix', fontsize=16)

    # --- Row 1: Images ---
    axs[0, 0].imshow(pixels_orig, cmap='gray')
    axs[0, 0].set_title("Original (Grayscale)")
    axs[0, 0].axis('off')

    axs[0, 1].imshow(pixels_halftone, cmap='gray')
    axs[0, 1].set_title("Halftone (Bayer 4x4)")
    axs[0, 1].axis('off')

    # --- Row 2: Histograms ---
    # Original Histogram
    axs[1, 0].hist(pixels_orig.ravel(), bins=256, color='gray', range=(0, 256))
    axs[1, 0].set_title("Original Histogram")
    axs[1, 0].set_xlabel("Pixel Intensity")
    axs[1, 0].set_ylabel("Frequency")

    # Halftone Histogram
    axs[1, 1].hist(pixels_halftone.ravel(), bins=256, color='black', range=(0, 256))
    axs[1, 1].set_title("Halftone Histogram (Binary)")
    axs[1, 1].set_xlabel("Pixel Intensity")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Paste your image path here
process_and_plot("C:...")
