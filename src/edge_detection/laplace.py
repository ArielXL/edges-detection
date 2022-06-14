import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplace(image, print=False):

    # convertir a imagen en escala de grises
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detectar los bordes mediante el metodo Laplace
    laplace = cv2.Laplacian(image, cv2.CV_64F)
    laplace = np.uint8(np.absolute(laplace))

    if print:
        images = [ image, laplace ]
        fig, axs = plt.subplots(1, len(images))

        for idx,image in enumerate(images):
            axs[idx].imshow(image, cmap='gray')

        plt.show()
    return laplace

def main():
    
    path = '../../img/cameraman.tif'
    image = cv2.imread(path)

    laplace(image, print=True)

if __name__ == '__main__':
    main()
