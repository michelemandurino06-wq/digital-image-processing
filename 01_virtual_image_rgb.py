# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 1. Load the color image
img = cv2.imread('...')

# Verify that the image has been correctly loaded
if img is None:
    print("Error: Image not found.")
else:
    # 2. Split the image into three channels
    # Note: OpenCV channel order is BGR (Blue, Green, Red)
    b, g, r = cv2.split(img)

    # --- OPTION 1: Save channels as grayscale ---
    # In these images, white represents the maximum intensity of the channel
    cv2.imwrite('channel_red_gray.png', r)
    cv2.imwrite('channel_green_gray.png', g)
    cv2.imwrite('channel_blue_gray.png', b)

    # --- OPTION 2: Save channels while preserving color visibility ---
    # Create a zero matrix with the same dimension as a channel
    zeros = np.zeros_like(b)

    # Merge channels by zeroing out unused channels
    # Format for cv2.merge: [Blue, Green, Red]
    img_red = cv2.merge([zeros, zeros, r])
    img_green = cv2.merge([zeros, g, zeros])
    img_blue  = cv2.merge([b, zeros, zeros])

    # Salva le immagini colorate
    cv2.imwrite('just_red.png', img_red)
    cv2.imwrite('just_green.png', img_green)
    cv2.imwrite('just_blue.png', img_blue)

    print("Processing complete. Files have been saved.")
