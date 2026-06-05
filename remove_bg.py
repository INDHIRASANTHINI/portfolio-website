#!/usr/bin/env python3
import sys
import subprocess

# Install rembg if not available
try:
    from rembg import remove
except ImportError:
    print("Installing rembg...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "rembg"])
    from rembg import remove

from PIL import Image
import io

# Load image
input_path = "images/profile.jpeg"
output_path = "images/profile.jpeg"

print(f"Processing {input_path}...")
with open(input_path, 'rb') as i:
    input_data = i.read()

# Remove background
output_data = remove(input_data)

# Save result
with open(output_path, 'wb') as o:
    o.write(output_data)

print(f"Background removed and saved to {output_path}")
