import cv2
import pylab
import numpy as np
import skimage.filters.edges
import matplotlib.pyplot as plt


def prewitt(image, path='', save=False, show=False):
    '''
    Deteccion de bordes mediante el operador de Prewitt.
    '''
    # convertir a imagen en escala de grises
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detectar los bordes mediante el metodo Canny
    imgage_gaussian = cv2.GaussianBlur(image, (3, 3), 0)

    kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

    prewitt_x = cv2.filter2D(imgage_gaussian, -1, kernel_x)
    prewitt_y = cv2.filter2D(imgage_gaussian, -1, kernel_y)

    prewitt = prewitt_x + prewitt_y
    # prewitt1 = skimage.filters.edges.prewitt(image)

    if show:
        # show_image(prewitt1)
        show_image(prewitt)
        # show_images([image, prewitt1])
        show_images([image, prewitt])
    if save:
        name = get_name_image(path)
        # save_image(prewitt1, f'../../img/{name}_prewitt1.png')
        save_image(prewitt, f'../../img/{name}_prewitt.png')

    return prewitt


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

    prewitt(image, path=path, save=True, show=True)


if __name__ == '__main__':
    main()
