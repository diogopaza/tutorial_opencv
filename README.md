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

print( "Altura(height): %d pixels" %( imagem.shape[0])) == exixbi a alatura em pixels
print( "Largura(width): %d pixels" %( imagem.shape[1])) == exixbi a largura em pixels
print("Canais(channels): %d" %(imagem.shape[2])) == 

<p>**Canais de uma imagem são responsáveis por armazenar informações de quantidade de cor. No caso de uma imagem
em escalas de cinza(****que formam uma foto preto e branco****), um canal é suficiente para informar a quantidade de cor em cada pixel. Para uma imagem colorida, mais canais são necesários. Em uma imagem padrão RGB é preciso 3 canais para armazenar a aquantidade de vermelhor( red ), verde( green ) e azul( blue ) existentes na imagem</p>
 