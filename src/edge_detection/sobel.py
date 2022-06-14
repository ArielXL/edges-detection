import cv2
import numpy as np
import matplotlib.pyplot as plt

def sobel(image, print=False):

    # convertir a imagen en escala de grises
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # gradiente de direccion x
    sobel_x = cv2.Sobel(image,cv2.CV_64F, 1, 0)
    # gradiente de direccion y
    sobel_y = cv2.Sobel(image,cv2.CV_64F, 0, 1)

    # gradiente de direccion x valor absoluto
    sobel_x = np.uint8(np.absolute(sobel_x))
    # gradiente de direccion y valor absoluto
    sobel_y = np.uint8(np.absolute(sobel_y))
    
    sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)

    if print:
        images = [ image, sobel_x, sobel_y, sobel_combined ]
        fig, axs = plt.subplots(1, len(images))

        for idx,image in enumerate(images):
            axs[idx].imshow(image, cmap='gray')

        plt.show()

    return sobel_combined

def main():

    path = '../../img/cameraman.tif'
    image = cv2.imread(path)

    sobel(image, print=True)

if __name__ == '__main__':
    main()
 
 
