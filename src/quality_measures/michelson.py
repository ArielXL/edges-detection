import numpy as np
import matplotlib.pyplot as plt

from skimage import data, img_as_float


def michelson_contrast(img):

    pixels = get_pixels(img)
    rows, columns = len(pixels), len(pixels[0])
    f_minimumm, f_maximumm = 300, -300

    for i in range(rows):
        for j in range(columns):
            f_minimumm = min(f_minimumm, pixels[i][j])
            f_maximumm = max(f_maximumm, pixels[i][j])

    michelson = (f_maximumm - f_minimumm) / (f_maximumm + f_minimumm)
    return michelson


def michelson(image1, image2, show=False):

    michelson_image1 = michelson_contrast(image1)
    michelson_image2 = michelson_contrast(image2)

    if show:
        show_images(image1, image2, michelson_image1, michelson_image2)

    return michelson_image2


def get_pixels(img):
    '''
    Devuelve la imagen en forma matricial.
    '''
    pixels = np.asarray(img)
    return pixels


def show_images(img1, img2, mse_img1, mse_img2):
    _, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4),
                           sharex=True, sharey=True)
    ax = axes.ravel()

    label = 'MICHELSON: {:.3f}'

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

    michelson_value = michelson(img, img_noise, show=True)
    print('El contraste de Michelson es %0.3f.' % michelson_value)


if __name__ == '__main__':
    main()
