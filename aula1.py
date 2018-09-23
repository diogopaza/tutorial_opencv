import cv2

imagem = cv2.imread('lampada.png')
cv2.imshow("original", imagem)
print( "Altura(height): %d pixels" %( imagem.shape[0]))
print( "Largura(width): %d pixels" %( imagem.shape[1]))
print("Canais(channels): %d" %(imagem.shape[2]))
