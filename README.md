# Digital Image Processing Pipeline

A modular implementation of fundamental digital image processing algorithms, focusing on color space conversions, halftoning/dithering techniques, and image compression schemes.

---

## Overview

This repository provides from-scratch implementations and comparative benchmarks for essential raster image manipulation techniques:

* **RGB to Grayscale Conversion**
  * Weighted luminance methods ($ITU\text{-}R\ BT.601$ and $BT.709$)
  * Arithmetic average and lightness/desaturation algorithms
* **Halftoning & Dithering**
  * **Thresholding**: Static global thresholding and dynamic/random thresholding
  * **Ordered Dithering**: Bayer matrix implementation with scalable thresholds ($2 \times 2$, $4 \times 4$, $8 \times 8$)
* **Image Compression**
  * **Lossless**: Run-Length Encoding (RLE) and basic Huffman coding
  * **Lossy**: Quantization-based and spatial-to-frequency domain encoding (DCT/JPEG-like pipeline)

---

## Tech Stack & Requirements

* **Language**: Python 3.10+ *(or C++ / Rust)*
* **Core Libraries**: NumPy, Pillow / OpenCV *(for I/O and display)*, Matplotlib

---

## Getting Started

# Clone the repository
git clone https://github.com/michelemandurino06-wq/Digital-Image-Processing.git
cd Digital-Image-Processing

# Install required dependencies
pip install -r requirements.txt

# Run any script directly (example: Bayer dithering)
python "4. bayer_halftone_v1.py"
