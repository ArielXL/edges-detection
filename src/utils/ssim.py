import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.metrics import structural_similarity

def ssim(image1, image2, print=False):

    ssim_image1 = structural_similarity(image1, image1, 
                    data_range=(image1.max()-image1.min()), multichannel=True)
    ssim_image2 = structural_similarity(image1, image2, 
                    data_range=(image2.max()-image2.min()), multichannel=True)

    if print:
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4),
                            sharex=True, sharey=True)
        ax = axes.ravel()

        label = 'SSIM: {:.3f}'

        ax[0].imshow(image1, cmap=plt.cm.gray, vmin=0, vmax=1)
        ax[0].set_xlabel(label.format(ssim_image1))
        ax[0].set_title('IMAGEN ORIGINAL')

        ax[1].imshow(image2, cmap=plt.cm.gray, vmin=0, vmax=1)
        ax[1].set_xlabel(label.format(ssim_image2))
        ax[1].set_title('OTRA IMAGEN')

        plt.tight_layout()
        plt.show()

    return ssim_image2

def main():

    img = img_as_float(data.horse())

    noise = np.ones_like(img) * 0.2 * (img.max() - img.min())
    noise[np.random.random(size=noise.shape) > 0.5] *= -1

    img_noise = img + noise

    ssim_value = ssim(img, img_noise, print=True)
    print('El indice de similitud estructural (SSIM) es %0.3f.' % ssim_value)

if __name__ == '__main__':
    main()
