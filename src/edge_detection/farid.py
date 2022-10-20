import cv2
import pylab
import skimage.filters.edges
import matplotlib.pyplot as plt


def farid(image, path='', save=False, show=False):
    '''
    Deteccion de bordes mediante el operador de Farid.
    '''
    # convertir a imagen en escala de grises
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detectar los bordes mediante el metodo Farid
    farid = skimage.filters.edges.farid(image)

    if show:
        show_image(farid)
        show_images([image, farid])
    if save:
        name = get_name_image(path)
        save_image(farid, f'../../img/{name}_farid.png')

    return farid


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

    path = '../../img/cameraman.tif'
    image = load_image(path)

    farid(image, path=path, save=True, show=True)


if __name__ == '__main__':
    main()
