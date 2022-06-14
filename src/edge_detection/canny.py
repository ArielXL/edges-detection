import cv2
import matplotlib.pyplot as plt

def canny(image, print=False):

    # convertir a imagen en escala de grises
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detectar los bordes mediante el metodo Canny
    canny = cv2.Canny(image, 30, 150)

    if print:
        images = [ image, canny ]
        fig, axs = plt.subplots(1, len(images))

        for idx,image in enumerate(images):
            axs[idx].imshow(image, cmap='gray')

        plt.show()
    return canny

def main():
    
    path = '../../img/cameraman.tif'
    image = cv2.imread(path)

    canny(image, print=True)

if __name__ == '__main__':
    main()
