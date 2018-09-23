import cv2

imagem = cv2.imread('lampada.png')
"""
cv2.imshow("original", imagem)
print( "Altura(height): %d pixels" %( imagem.shape[0]))
print( "Largura(width): %d pixels" %( imagem.shape[1]))
print("Canais(channels): %d" %(imagem.shape[2]))
"""
(b, g, r) = imagem[0,0]
print("Cor do pixel em (0,0) - Vermelho: %d Verde: %d Azul: %d" %(r, g ,b))


(b, g, r) = imagem[30, 250]
print ("Cor do pixel em (250, 30) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))
"""
imagem[ 10:50, 10:200] = ( 0, 0, 255)
cv2.imshow('modificada', imagem)
"""

fatia = imagem[0:200, 200:300]
cv2.imshow('Imagem Fatiada', fatia)

cv2.imwrite('imagemFatiada.png', fatia)
