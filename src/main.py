import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from utils.mse import mse
from utils.psnr import psnr
from utils.ssim import ssim
from edge_detection.canny import canny
from edge_detection.sobel import sobel
from edge_detection.laplace import laplace

class HomeWork2:

    def __init__(self, image, outskirt='canny'):
        '''
        Inicializa las variables a utilizar y llev a cabo el pipeline.
        '''
        self.methods_outskirts = {
            'canny'     : canny,
            'laplace'   : laplace,
            'sobel'     : sobel
        }

        if outskirt not in self.methods_outskirts:
            raise Exception(f"El metodo '{outskirt}' no esta definido para la deteccion de bordes.")
        
        self.outskirt = self.methods_outskirts[outskirt]
        self.image = image
        self.image_outskirt = self.outskirt(self.image)

        self.show_images([ self.image, self.image_outskirt ])
        self.new_image = self.sum_image(self.image, self.image_outskirt)
        self.print_results()

    def show_image(self, image):
        '''
        Muestra la imagen especificada.
        '''
        plt.imshow(image, cmap='gray')
        plt.show()

    def show_images(self, images):
        '''
        Muestra las imagenes especificadas.
        '''
        count_image = len(images)
        fig, axs = plt.subplots(1, count_image)

        for idx,image in enumerate(images):
            axs[idx].imshow(image, cmap='gray')

        plt.show()

    def save_image(self, image, path):
        '''
        Guarda la imagen en la ruta especificada.
        '''
        cv2.imwrite(path, image)

    def get_image(self, pixels):
        '''
        Convierte de una matriz a imagen.
        '''
        array = np.array(pixels, dtype=np.uint8)
        image = Image.fromarray(array)
        return image

    def get_pixels(self, image):
        '''
        Devuelve la imagen en forma matricial.
        '''
        pixels = np.asarray(image)
        return pixels

    def sum_image(self, img1, img2):
        '''
        Efectua la suma de las imagenes especificadas.
        '''
        pixels_img1 = self.get_pixels(img1)
        pixels_img2 = self.get_pixels(img2)
        new_pixels = []
        rows, columns = len(pixels_img1), len(pixels_img1[0])

        for i in range(rows):
            new_pixels.append([])
            for j in range(columns):
                values = pixels_img1[i][j] + pixels_img2[i][j]
                values = [ 255 if value > 255 else value for value in values ]
                new_pixels[i].append(values)

        image = self.get_image(new_pixels)
        # self.show_image(image)
        return image

    def print_results(self):
        '''
        Imprime los resultados de las medidas de contraste 
        de calidad segun las imagenes procesadas.
        '''
        mse_value = mse(self.image, np.array(self.new_image))
        psnr_value = psnr(self.image, np.array(self.new_image))
        ssim_value = ssim(self.image, np.array(self.new_image))

        print('El error cuadratico medio (MSE) es %0.3f.' % mse_value)
        print('El valor PSNR es %0.3f dB.' % psnr_value)
        print('El indice de similitud estructural (SSIM) es %0.3f.' % ssim_value)

def main():
    
    path = '../img/cameraman.tif'
    img = cv2.imread(path)

    HomeWork2(img, outskirt='canny')

if __name__ == '__main__':
    main()
