import qrcode 
import numpy as np

# Create QR code object 
qr = qrcode.QRCode(version=1, box_size=4, border=1)
qr.add_data('https://www.eyeson.com')
qr.make(fit=True)

# Get the QR matrix size  
matrix = qr.get_matrix()
size = matrix.shape[0]

# Generate mask matching matrix size 
mask = np.zeros((size, size), dtype=bool)
center = size // 2
for i in range(size):
    for j in range(size):
        if (i - center) ** 2 + (j - center) ** 2 < 8 ** 2:
            mask[i, j] = True
            
# Generate image with mask applied
img = qr.make_image(image_factory=None, mask_pattern=mask) 

# Save the image
img.save('rounded_qrcode.png')