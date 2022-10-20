import cv2
import pylab
import numpy as np
import skimage.filters.edges
import matplotlib.pyplot as plt


def scharr(image, path='', save=False, show=False):
    '''
    Deteccion de bordes mediante el operador de Scharr.
    '''
    # convertir a imagen en escala de grises
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # computa la primera derivada de Sobel en el eje x
    scharr_x = cv2.Scharr(image, cv2.CV_64F, 1, 0)
    # computa la primera derivada de Sobel en el eje x
    scharr_y = cv2.Scharr(image, cv2.CV_64F, 0, 1)

    # gradiente de direccion x valor absoluto
    scharr_x = np.uint8(np.absolute(scharr_x))
    # gradiente de direccion y valor absoluto
    scharr_y = np.uint8(np.absolute(scharr_y))

    scharr1 = cv2.bitwise_or(scharr_x, scharr_y)
    scharr = skimage.filters.edges.scharr(image)

    if show:
        show_image(scharr)
        # show_image(scharr1)
        show_images([image, scharr])
    if save:
        name = get_name_image(path)
        save_image(scharr, f'../../img/{name}_scharr.png')

    return scharr


def get_name_image(path):
    '''
    Devuelve el nombre de la imagen segun la ruta.
    '''
    name_extention = path.split('/')[-1]
    name, _ = name_extention.split('.')
    return name


def load_image(path):
    '''
    Carga la imagen desde la ruta especificada.
    '''
    img = cv2.imread(path)
    return img


def show_image(image):
    '''
    Muestra la imagen especificada.
    '''
    plt.imshow(image, cmap='gray')
    plt.show()


def show_images(images):
    '''
    Muestra las imagenes especificadas.
    '''
    count_image = len(images)
    _, axs = plt.subplots(1, count_image)

    for idx, image in enumerate(images):
        axs[idx].imshow(image, cmap='gray')

    plt.show()


def save_image(image, path):
    '''
    Guarda la imagen en la ruta especificada.
    '''
    pylab.gray()
    pylab.imsave(path, image)


def main():

    path = '../../img/lena.tif'
    image = load_image(path)

    scharr(image, path=path, save=True, show=True)


if __name__ == '__main__':
    main()
