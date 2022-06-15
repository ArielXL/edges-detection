import numpy as np
from math import log10
from skimage import data, img_as_float
from skimage.metrics import mean_squared_error
  
def psnr(image, image_noise):

    mse = mean_squared_error(image, image_noise)
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel) - 10 * log10(mse)

    return psnr
  
def main():

    img = img_as_float(data.camera())

    noise = np.ones_like(img) * 0.2 * (img.max() - img.min())
    noise[np.random.random(size=noise.shape) > 0.5] *= -1

    img_noise = img + noise

    psnr_value = psnr(img, img_noise)
    print('El valor PSNR es %0.3f dB.' % psnr_value)
       
if __name__ == "__main__":
    main()