import cv2

imagem = cv2.imread('lampada.jpg')
inverter = cv2.flip(imagem, -1)



cv2.imshow('minha_imagem2', inverter)
