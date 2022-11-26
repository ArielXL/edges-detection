import numpy as np
import matplotlib.pyplot as plt

from skimage import data, img_as_float
from skimage.metrics import mean_squared_error


def mse(image1, image2, show=False):

    mse_image1 = mean_squared_error(image1, image1)
    mse_image2 = mean_squared_error(image1, image2)

    if show:
        show_images(image1, image2, mse_image1, mse_image2)

    return mse_image2


def show_images(img1, img2, mse_img1, mse_img2):
    _, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4),
                           sharex=True, sharey=True)
    ax = axes.ravel()

    label = 'MSE: {:.3f}'

    ax[0].imshow(img1, cmap=plt.cm.gray, vmin=0, vmax=1)
    ax[0].set_xlabel(label.format(mse_img1))
    ax[0].set_title('IMAGEN ORIGINAL')

    ax[1].imshow(img2, cmap=plt.cm.gray, vmin=0, vmax=1)
    ax[1].set_xlabel(label.format(mse_img2))
    ax[1].set_title('IMAGEN CON RUIDO')

    plt.tight_layout()
    plt.show()


def main():

    img = img_as_float(data.coins())

    noise = np.ones_like(img) * 0.2 * (img.max() - img.min())
    noise[np.random.random(size=noise.shape) > 0.5] *= -1

    img_noise = img + noise

    mse_value = mse(img, img_noise, show=True)
    print('El error cuadrático medio (MSE) es %0.3f.' % mse_value)


if __name__ == '__main__':
    main()
