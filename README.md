<h1>Básico do OpenCV com Python</h1>
<a href="http://www.galirows.com.br/meublog/blog/basico-opencv-python-mostrar-imagem/">link do tuorial</a>
<p>Tutorial para manipular imagens com OpenCV usando o Python. </p>

<h4>Carregar e mostrar imagens</h4>
<p>Usando o método imread() que espera como parâmetro o enderço da imagem, </p>
<p>Para mostrar a imagem é utilizado o metodo imshow(), o método espera um nome como primeiro parametro e o objeto de imagem.</p>

//Exemplo:

import cv2
imagem = cv2.imread("lampada.png")
cv2.imshow("Imagem Original", imagem)