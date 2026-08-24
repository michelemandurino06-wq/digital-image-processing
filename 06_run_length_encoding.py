# -*- coding: utf-8 -*-
from PIL import Image

# 1. GET THE PATH (Paste the path to your image here)
image_path = input("Drag the image here or enter path: ").strip().replace('"', '')

# 2. OPEN AND CONVERT TO LIST OF VALUES
img = Image.open(image_path).convert('L')
original_pixels = list(img.getdata())

# 3. RLE COMPRESSION
compressed_data = []
if original_pixels:
    previous_pixel = original_pixels[0]
    counter = 0
    
    for pixel in original_pixels:
        if pixel == previous_pixel:
            counter += 1
        else:
            compressed_data.append((counter, previous_pixel))
            previous_pixel = pixel
            counter = 1
    
    # Save the last run
    compressed_data.append((counter, previous_pixel))

# 4. DISPLAY RESULTS
print(f"\nOriginal pixels: {len(original_pixels)}")
print(f"RLE pairs created: {len(compressed_data)}")

# Visual preview of the output
print(f"\nFirst 5 runs (Count, Color): {compressed_data[:5]}")
