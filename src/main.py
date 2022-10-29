import numpy as np

from utils.images import Images

from quality_measures.mse import mse
from quality_measures.psnr import psnr
from quality_measures.ssim import ssim
from quality_measures.michelson import michelson

from edge_detection.canny import canny
from edge_detection.sobel import sobel
from edge_detection.farid import farid
from edge_detection.scharr import scharr
from edge_detection.laplace import laplace
from edge_detection.prewitt import prewitt
from edge_detection.roberts import roberts


class EdgeDetection:

    def __init__(self, path='../img/cameraman.tif', save=False, show=False):
        '''
        Inicializa las variables a utilizar y llev a cabo el pipeline.
        '''
        self.methods_outskirts = {
            'canny': canny,
            'farid': farid,
            'laplace': laplace,
            'prewitt': prewitt,
            'scharr': scharr,
            'roberts': roberts,
            'sobel': sobel
        }
        self.path = path
        self.save = save
        self.show = show
        self.image = Images.LoadImage(self.path)

    def run_edge_detection(self, outskirt='canny'):

        if outskirt not in self.methods_outskirts:
            raise Exception(
                f"El método '{outskirt}' no está definido para la detección de bordes.")

        self.outskirt = self.methods_outskirts[outskirt]
        self.image_outskirt = self.outskirt(self.image)

        if self.save:
            name = Images.GetNameImage(self.path)
            Images.SaveImage(self.image_outskirt,
                             f'../img/{name}_{outskirt}.png')

        if self.show:
            Images.ShowImage(self.image_outskirt)
            Images.ShowImages([self.image, self.image_outskirt])

    def print_results(self):
        '''
        Imprime los resultados de las medidas de contraste 
        de calidad segun las imagenes procesadas.
        '''
        new_image = Images.GetSumImage(self.image, self.image_outskirt)
        arr = np.array(new_image)

        mse_value = mse(self.image, arr)
        psnr_value = psnr(self.image, arr)
        ssim_value = ssim(self.image, arr)
        michelson_value = michelson(self.image, arr)

        print('El error cuadrático medio (MSE) es %0.3f.' % mse_value)
        print('El valor PSNR es %0.3f dB.' % psnr_value)
        # print('El índice de similitud estructural (SSIM) es %0.3f.' % ssim_value)
        print('El contraste de Michelson es %0.3f.' % michelson_value)


def run(paths, operators):

    for path in paths:
        edge_detection = EdgeDetection(path=path, save=True, show=False)
        for operator in operators:
            edge_detection.run_edge_detection(outskirt=operator)
            edge_detection.print_results()


def main():

    paths = ['../img/cameraman.tif', '../img/house.tif',
             '../img/lake.tif', '../img/lena.tif',
             '../img/livingroom.tif', '../img/peppers.tif',
             '../img/pirate.tif', '../img/jetplane.tif',
             '../img/mandril.tif']
    operators = ['canny', 'farid', 'laplace',
                 'prewitt', 'roberts', 'scharr', 'sobel']

    run(paths, operators)


if __name__ == '__main__':
    main()
