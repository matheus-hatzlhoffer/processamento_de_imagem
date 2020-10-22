########################################
## Nome: Matheus Carvalho Hatzlhoffer ##
## RA : 222174                        ##
########################################

import cv2
import numpy as np
import matplotlib.pyplot as plt

def salvaImagem(nome_da_foto , foto):
    file = "output/"
    plt.imsave(file+nome_da_foto, foto, cmap="gray")
    return

def showImage(img):
    plt.imshow(img, cmap='gray')
    plt.show()
    return

#coloca a imagem em negativo
def imgNegativo(img):
    img_negativo = img * (-1) + 255
    return img_negativo

#Faz o espelhamenro vertical
def espelhamentoVertical(img):
    img_espelhada = np.flipud(img)
    return img_espelhada

#coloca os valores do pixel entre 100 e 200 e arredonda
def intensidadeTransformada(img):
    img_transformada = np.around(img*(0.3921)+100).astype(int)
    return img_transformada

#verifica se os valores dos pixels estão entre 100 e 200
def verificaIntensidadeRange(img):
    if(img.min()>=100 and img.max()<=200):
        print("A imagem tem intensidade entre 100 e 200")
    else:
        print("A imagem não tem intensidade entre 100 e 200")
    return

#as linhas pares são escritas da esquerda para a direita
def inverteLinhasPares(img):
    img_linhas_invertidas = np.copy(img)
    img_linhas_invertidas[::2] = np.fliplr(img_linhas_invertidas[::2]) 
    return img_linhas_invertidas

# Espelha a imagem do meio para o fim verticalmente
# código inspirado em https://stackoverflow.com/questions/40837224/matrix-mirroring-in-python
def imgEspelhada(img):
    if(len(img)%2):
        img_espelhada = list(img[:round(len(img)/2)])
        img_espelhada.extend(img_espelhada[0:-1])
    else:
        img_espelhada = list(img[:(len(img)//2)])
        img_espelhada.extend(img_espelhada[::-1])
    return np.array(img_espelhada)

#Faz o ajuste de brilho com o valor y
def ajusteBrilho(img, y):
    if(y<=0):
        print ("O valor de gama é inválido, nenhuma alteração feita")
        return img
    img_brilho = (img/255)**(1/y)
    img_brilho = img_brilho*255
    return np.round(img_brilho).astype(int)

#Usa uma matriz máscara para pegar o plano de bit indicado
#voltar aqui para ver se faz sentid0
def planoDeBit(img, bit):
    if(bit<0 or bit>7):
        print("O valor do bit precisa estar entre 0 e 7. Nenhuma alteração feita")
        return img
    mascara = np.full(img.shape, (2**(bit+1))-1)
    print(img.shape)
    print(mascara.shape)
    print(mascara[0][0])
    plano_de_bit = np.bitwise_and(img, mascara)
    return plano_de_bit

#Ainda precisa ser implementado
def mosaico(img):
    return 0

#Combina duas imagens de acordo com uma média ponderada das duas proporções
def combinacaoDeImagem(img1, img2, propimg1, propimg2):
    if(img1.shape != img2.shape):
        print("As imagens devem ter o mesmo tamanho. Nenhuma alteração feita")
        return 0
    elif(propimg1 < 0 or propimg2 < 0):
        print("As proporções de cada imagem não podem ser negativas")
        return 0 
    img_combinada = np.round((propimg1*img1+propimg2*img2)/(propimg1+propimg2)).astype(int)
    return img_combinada


# open images files and store they in a numpy array
img_baboon = np.array(plt.imread('input/baboon.png', cv2.IMREAD_GRAYSCALE))
img_butterfly = np.array(plt.imread('input/butterfly.png', cv2.IMREAD_GRAYSCALE))
img_city = np.array(plt.imread('input/city.png', cv2.IMREAD_GRAYSCALE))

#Cria as imagens conforme os exemplos da tarefa 0
img_city_negativa = imgNegativo(img_city)
img_city_espelhada_vertical = espelhamentoVertical(img_city)
img_city_transformada = intensidadeTransformada(img_city)
img_city_inverte_linhas = inverteLinhasPares(img_city)
img_city_reflexao = imgEspelhada(img_city)
img_baboon_brilho1 = ajusteBrilho(img_baboon, 1.5)
img_baboon_brilho2 = ajusteBrilho(img_baboon, 2.5)
img_baboon_brilho3 = ajusteBrilho(img_baboon, 3.5)
#img_baboon_bit1 = planoDeBit(img_baboon, 0)
img_baboon_bit2 = planoDeBit(img_baboon, 4)
img_baboon_bit3 = planoDeBit(img_baboon, 7)
img_combinada1 = combinacaoDeImagem(img_baboon, img_butterfly, 0.2, 0.8)
img_combinada2 = combinacaoDeImagem(img_baboon, img_butterfly, 0.5, 0.5)
img_combinada3 = combinacaoDeImagem(img_baboon, img_butterfly, 0.8, 0.2)

#salva as fotos no diretório output
salvaImagem("city_negativa.png", img_city_negativa)
salvaImagem("city_espelhada_vertical.png", img_city_espelhada_vertical)
salvaImagem("city_transformada.png", img_city_transformada)
salvaImagem("city_linhas_invertidas.png", img_city_inverte_linhas)
salvaImagem("city_reflexao.png", img_city_reflexao)
salvaImagem("baboon_brilho1.png", img_baboon_brilho1)
salvaImagem("baboon_brilho2.png", img_baboon_brilho2)
salvaImagem("baboon_brilho3.png", img_baboon_brilho3)
salvaImagem("baboon_bit1.png", img_baboon_bit1)
salvaImagem("baboon_bit2.png", img_baboon_bit2)
salvaImagem("baboon_bit3.png", img_baboon_bit3)
salvaImagem("combinacao_de_imagem1.png", img_combinada1)
salvaImagem("combinacao_de_imagem2.png", img_combinada2)
salvaImagem("combinacao_de_imagem3.png", img_combinada3)

#Mostra as imagens gerados pelo matplotlib.pyplot
showImage(img_city_negativa)
showImage(img_city_espelhada_vertical)
showImage(img_city_transformada)
showImage(img_city_inverte_linhas)
showImage(img_city_reflexao)
showImage(img_baboon_brilho1)
showImage(img_baboon_brilho2)
showImage(img_baboon_brilho3)
showImage(img_baboon_bit1)
showImage(img_baboon_bit2)
showImage(img_baboon_bit3)
showImage(img_combinada1)
showImage(img_combinada2)
showImage(img_combinada3)
