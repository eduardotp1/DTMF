# Camada Física - Projeto 2 - DTMF
Gabriel Moreira e Eduardo Tirta

## Geração de tons
 Cada tom é uma combinação de duas senoides de frequências diferentes, seguindo a tabela DMTF, as senoides foram geradas utilizando a biblioteca numpy, e depois somadas, formando uma senoide única.
 
 ### Representação
 ![Representação](imgs/info/info.001.jpeg)
 
## Frequências de composição dos tons
 O tom segue o padrão das frequências da tabela abaixo.

| **Hz**  |**1209**|**1336**|**1633**|
| --------| -------| ------ | ------ |
| **697** |    1   |    2   |    3   |
| **770** |    4   |    5   |    6   |
| **852** |    7   |    8   |    9   |
| **941** |        |    0   |        |

## Gráficos de resposta dos tons


| Tom |                 Original                  |             Resposta             |
|-----| ----------------------------------------- | -------------------------------- |
|  1  |![Tom número 1](imgs/tone_original1.png)   | ![Tom número 1](imgs/tone1.png)  |
|  2  | ![Tom número 1](imgs/tone_original2.png)  | ![Tom número 1](imgs/tones2.png) |
|  3  | ![Tom número 1](imgs/tone_original3.png)  | ![Tom número 1](imgs/tones3.png) |
|  4  | ![Tom número 1](imgs/tone_original4.png)  | ![Tom número 1](imgs/tone4.png)  |
|  5  | ![Tom número 1](imgs/tone_original5.png)  | ![Tom número 1](imgs/tone5.png)  |
|  6  | ![Tom número 1](imgs/tone_original6.png)  | ![Tom número 1](imgs/tone6.png)  |
|  7  | ![Tom número 1](imgs/tone_original7.png)  | ![Tom número 1](imgs/tone7.png)  |
|  8  | ![Tom número 1](imgs/tone_original8.png)  | ![Tom número 1](imgs/tone8.png)  |
|  9  | ![Tom número 1](imgs/tone_original9.png)  | ![Tom número 1](imgs/tone9.png)  |
|  0  | ![Tom número 1](imgs/tone_original0.png)  | ![Tom número 1](imgs/tone0.png)  |


A diferença entre o tom original e o recebido ocorre, principalmente, por captar ruídos do ambiente externo, além disso a uma perda que faz com que a amplitude do gráfico altere


| Tom |                 Original                  |             Resposta             |
|-----| ----------------------------------------- | -------------------------------- |
|  1  |![Tom número 1](imgs_f/fourier-o1.png)   | ![Tom número 1](imgs_f/fourier1.png)  |
|  2  | ![Tom número 1](imgs_f/fourier-o2.png)  | ![Tom número 1](imgs_f/fourier2.png) |
|  3  | ![Tom número 1](imgs_f/fourier-o3.png)  | ![Tom número 1](imgs_f/fourier3.png) |
|  4  | ![Tom número 1](imgs_f/fourier-o4.png)  | ![Tom número 1](imgs_f/fourier4.png)  |
|  5  | ![Tom número 1](imgs_f/fourier-o5.png)  | ![Tom número 1](imgs_f/fourier5.png)  |
|  6  | ![Tom número 1](imgs_f/fourier-o6.png)  | ![Tom número 1](imgs_f/fourier6.png)  |
|  7  | ![Tom número 1](imgs_f/fourier-o7.png)  | ![Tom número 1](imgs_f/fourier7.png)  |
|  8  | ![Tom número 1](imgs_f/fourier-o8.png)  | ![Tom número 1](imgs_f/fourier8.png)  |
|  9  | ![Tom número 1](imgs_f/fourier-o9.png)  | ![Tom número 1](imgs_f/fourier9.png)  |
|  0  | ![Tom número 1](imgs_f/fourier-o0.png)  | ![Tom número 1](imgs_f/fourier0.png)  |

