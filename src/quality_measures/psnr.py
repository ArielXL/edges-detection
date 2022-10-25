import numpy as np
from math import log10
import matplotlib.pyplot as plt

from skimage import data, img_as_float
from skimage.metrics import mean_squared_error


def peek_signal_noise_ratio(img1, img2):

    mse = mean_squared_error(img1, img2)
    max_pixel = 255.0

    if mse == 0:
        psnr = 0
    else:
        psnr = 20 * log10(max_pixel) - 10 * log10(mse)

    return psnr


def psnr(image1, image2, show=False):

    psnr_image1 = peek_signal_noise_ratio(image1, image1)
    psnr_image2 = peek_signal_noise_ratio(image1, image2)

    if show:
        show_images(image1, image2, psnr_image1, psnr_image2)

    return psnr_image2


def show_images(img1, img2, psnr_img1, psnr_img2):
    _, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4),
                           sharex=True, sharey=True)
    ax = axes.ravel()

    label = 'PSNR: {:.3f} db'

    ax[0].imshow(img1, cmap=plt.cm.gray, vmin=0, vmax=1)
    ax[0].set_xlabel(label.format(psnr_img1))
    ax[0].set_title('IMAGEN ORIGINAL')

    ax[1].imshow(img2, cmap=plt.cm.gray, vmin=0, vmax=1)
    ax[1].set_xlabel(label.format(psnr_img2))
    ax[1].set_title('IMAGEN CON RUIDO')

    plt.tight_layout()
    plt.show()


def main():

    img = img_as_float(data.camera())

    noise = np.ones_like(img) * 0.2 * (img.max() - img.min())
    noise[np.random.random(size=noise.shape) > 0.5] *= -1

    img_noise = img + noise

    psnr_value = psnr(img, img_noise, show=True)
    print('El valor PSNR es %0.3f dB.' % psnr_value)


if __name__ == "__main__":
    main()
