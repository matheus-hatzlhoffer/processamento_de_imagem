import cv2
import kernel
import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy.ndimage as ndimage

def showImage(img):
    plt.imshow(img, cmap='gray')
    plt.show()
    return

def saveImage(file_name , img):
    directory = "Trabalho1/output/"
    plt.imsave(directory+file_name+'.png', img, cmap="gray")
    return

def covolution(image, kernel):
    fliped_kernel = kernel[::-1,::-1] #perform a 180 degree rotation of the kernel
    return cv2.filter2D(image, -1, fliped_kernel)


if(len(sys.argv) == 4):
    image_name = sys.argv[1]
    kernel_name = sys.argv[2]
    output_name = sys.argv[3]
    image = np.array(cv2.imread('input/'+image_name ,cv2.IMREAD_GRAYSCALE))
    if(kernel_name == '1' or kernel_name == 'h1'):
        output = covolution(image, kernel.kernel_h1)
        saveImage(output_name, output)
        showImage(output)
    elif(kernel_name == '2' or kernel_name == 'h2'):
        output = covolution(image, kernel.kernel_h2)
        saveImage(output_name, output)
        showImage(output)
    elif(kernel_name == '3' or kernel_name == 'h3'):
        output = covolution(image, kernel.kernel_h3)
        saveImage(output_name, output)
        showImage(output)
    elif(kernel_name == '4' or kernel_name == 'h4'):
        output = covolution(image, kernel.kernel_h4)
        saveImage(output_name, output)
        showImage(output)
    elif(kernel_name == '5' or kernel_name == 'h5'):
        output = covolution(image, kernel.kernel_h5)
        saveImage(output_name, output)
        showImage(output)
    elif(kernel_name == '6' or kernel_name == 'h6'):
        output = covolution(image, kernel.kernel_h6)
        saveImage(output_name, output)
        showImage(output)
    elif(kernel_name == '7' or kernel_name == 'h7'):
        output = covolution(image, kernel.kernel_h7)
        saveImage(output_name, output)
        showImage(output)
    elif(kernel_name == '8' or kernel_name == 'h8'):
        output = covolution(image, kernel.kernel_h8)
        saveImage(output_name, output)
        showImage(output)
    elif(kernel_name == '9' or kernel_name == 'h9'):
        output = covolution(image, kernel.kernel_h9)
        saveImage(output_name, output)
        showImage(output)
    elif(kernel_name == '10' or kernel_name == 'h10'):
        output = covolution(image, kernel.kernel_h10)
        saveImage(output_name, output)
        showImage(output)
    elif(kernel_name == '11' or kernel_name == 'h11'):
        output = covolution(image, kernel.kernel_h11)
        saveImage(output_name, output)
        showImage(output)
    elif(kernel_name == '34' or kernel_name == 'h34' or kernel_name == 'h3h4'):
        output = ndimage.sobel(image, mode='mirror') ##igual ao cv2
        saveImage(output_name, output)
        showImage(output)
    else:
        print("Filtro não encontrado")
else:
    print("Número de argumentos inválido")
