import cv2
import pylab
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image


class Images:

    @staticmethod
    def LoadImage(path):
        '''
        Carga la imagen desde la ruta especificada.
        '''
        img = cv2.imread(path)
        return img

    @staticmethod
    def ShowImage(image):
        '''
        Muestra la imagen especificada.
        '''
        plt.imshow(image, cmap='gray')
        plt.show()

    @staticmethod
    def ShowImages(images):
        '''
        Muestra las imagenes especificadas.
        '''
        count_image = len(images)
        _, axs = plt.subplots(1, count_image)

        for idx, image in enumerate(images):
            axs[idx].imshow(image, cmap='gray')

        plt.show()

    @staticmethod
    def SaveImage(image, path):
        '''
        Guarda la imagen en la ruta especificada.
        '''
        pylab.gray()
        pylab.imsave(path, image)

    @staticmethod
    def GetNameImage(path):
        '''
        Devuelve el nombre de la imagen segun la ruta.
        '''
        name_extention = path.split('/')[-1]
        name, _ = name_extention.split('.')
        return name

    @staticmethod
    def GetImage(pixels):
        '''
        Convierte de una matriz a imagen.
        '''
        array = np.array(pixels, dtype=np.uint8)
        image = Image.fromarray(array)
        return image

    @staticmethod
    def GetPixels(image):
        '''
        Devuelve la imagen en forma matricial.
        '''
        pixels = np.asarray(image)
        return pixels

    @staticmethod
    def GetSumImage(img1, img2):
        '''
        Efectua la suma de las imagenes especificadas.
        '''
        pixels_img1 = Images.GetPixels(img1)
        pixels_img2 = Images.GetPixels(img2)
        new_pixels = []
        rows, columns = len(pixels_img1), len(pixels_img1[0])

        for i in range(rows):
            new_pixels.append([])
            for j in range(columns):
                values = pixels_img1[i][j] + pixels_img2[i][j]
                values = [255 if value > 255 else value for value in values]
                new_pixels[i].append(values)

        image = Images.GetImage(new_pixels)
        # Images.ShowImage(image)
        return image
