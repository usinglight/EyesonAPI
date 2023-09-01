import qrcode
import numpy as np

# Create the mask 
mask = np.zeros((21,21), dtype=bool)
for i in range(21):
    for j in range(21):
        if (i - 10) ** 2 + (j - 10) ** 2 < 8 ** 2:
            mask[i, j] = True

# Generate the QR Code using the mask            
qr = qrcode.QRCode(version=1, box_size=4, border=1)
qr.add_data('https://www.eyeson.com')
qr.make(fit=True)
img = qr.make_image(mask_pattern=mask)

img.save('rounded_qrcode.png')