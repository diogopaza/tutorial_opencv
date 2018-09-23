
import cv2

imagem = cv2.imread('a.jpg')

altura, largura = imagem.shape[:2]
print(altura)
print(largura)
ponto = (largura /2, altura/2)
rotacao = cv2.getRotationMatrix2D(ponto, 270, 1.0  )
rotacionando = cv2.warpAffine( imagem, rotacao, (largura, altura))
cv2.imshow('Imagem Rotacionada ', rotacionando)
