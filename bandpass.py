import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('1.jpg',0)

f=np.fft.fft2(img)
f=np.fft.fftshift(f)
bw=100
ew=100
rows,cols=img.shape
crow,ccol=rows//2,cols//2

ze=np.zeros((rows,cols))
# big square of ones
ze[crow-bw-ew:crow+bw+ew,ccol-bw-ew:ccol+bw+ew]=1
# small square of zeros
ze[crow-bw:crow+bw,ccol-bw:ccol+bw]=0

f2=f*ze

absf=np.abs(f2)
logabs=200*np.log(absf)
plt.subplot(121)
plt.imshow(logabs,cmap='gray')

imrecover=np.fft.ifftshift(f2)
imrecover=np.fft.ifft2(f2)
image=np.abs(imrecover)
plt.subplot(122)
plt.imshow(image,cmap='gray')


plt.show()
