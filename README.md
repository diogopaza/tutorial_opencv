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

print( "Altura(height): %d pixels" %( imagem.shape[0])) == exibi a altura em pixels<br>
print( "Largura(width): %d pixels" %( imagem.shape[1])) == exibi a largura em pixels<br>
print("Canais(channels): %d" %(imagem.shape[2])) == <br>

<p>**Canais de uma imagem são responsáveis por armazenar informações de quantidade de cor. No caso de uma imagem
em escalas de cinza(****que formam uma foto preto e branco****), um canal é suficiente para informar a quantidade de cor em cada pixel. Para uma imagem colorida, mais canais são necesários. Em uma imagem padrão RGB é preciso 3 canais para armazenar a aquantidade de vermelhor( red ), verde( green ) e azul( blue ) existentes na imagem</p>
 
 <h4>Pegando a cor de um pixel</h4>
<p>Completnado com o código abaixo será retornado a cor do pixel em determinada posição da matriz.</p>
(b, g, r) = imagem[0,0]
print("Cor do pixel em (0,0) - Vermelho: %d Verde: %d Azul: %d" %(r, g ,b))
<p>O padrão de cor do OpenCV é BGR e não RGB</p>
<p>Primeiro é informado a coluna e depois a linha, não seguindo o parão linha coluna.</p>
<p>Os resultados estão de 0 a 255 e representam a quantidade da cor existente no canal.</p>
<p>O 255 é o máximo de cada cor, ou seja o branco é a presença de todas as cores.</p>

<h4>Modificando o pixel de uma imagem</h4>
<p>No código abaixo as cores dos pixels são alteradas primeiro na vertical e depois na horizontal, os canais estão no padrão BGR</p>

imagem[ 10:50, 10:200] = ( 0, 0, 255)
cv2.imshow('modificada', imagem)
<h4>Recortar um pedaço da imagem</h4>

fatia = imagem[0:150, 150:300]
cv2.imshow('Imagem Fatiada', imagem)

<p>Para salvar a imagem usa-se o método inwrite()</p>

cv2.imwrite('imagemFatiada', fatia)

<h6>Exercícios</h6>
<p>1-Espelhamento da imagem, invertendo os pixles da esquerda para a parte da direita e vice-versa</p>




