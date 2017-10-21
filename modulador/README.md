# Projeto 3 - Modulação


## Modulação e demodulação

**Modulação**: é o método de variação de amplitude (no caso da modulação _AM_) de um sinal de acordo com uma frequência portadora definida anteriormente.

![Alt Text](./media/Amfm3-en-de.gif)

_Modulação em AM e FM_

---

**Demodulação**: para conseguir interpretar o sinal modulado recebido, deve multiplicar o sinal pela portadora, ou seja, fazer a modulação em cima de um sinal já modulado, assim, o sinal será deslocado novamente, conseguindo ser interpretado na origem.


## Frequências das portadoras utilizadas
As frequências portadoras escolhidas foram 9000 _Hz_ e 17000 _Hz_.

**Fourier portadora 1**

![Alt Text](./media/fp1.png)

---

 **Fourier portadora 2**

![Alt Text](./media/fp2.png)


## Bandas ocupadas

A banda ocupada pelo sinal é de 7000 _Hz_ pois assim que o arquivo de cada áudio é lido, o sinal passa por um filtro passa baixa que elimina frequências acima de 3500 _Hz_. Posteriormente é feita a modulação desse sinal cortado, ou seja, a parte negativa do áudio é deslocada de modo que tudo fique positivo. Deste modo, a banda passa a ter o dobro do seu tamanho cortado.

## Gráficos do processo

### Transmissor

**Sinais filtrados no tempo**

|           Sinal 1            |           Sinal 2        |
|------------------------------|--------------------------|
| ![sinal 1](media/f1.png)     | ![sinal 2](media/f2.png) | 

---

**Fourier dos sinais filtrados**

|           Sinal 1           |           Sinal 2        |
|-----------------------------|--------------------------|
| ![sinal 1](media/ff1.png)   | ![sinal 2](media/ff2.png)| 

---

**Fourier das portadoras**

|          Portadora 1                        |        Portadora 2       |
|-----------------------------                |--------------------------|
| ![sinal 1](media/fourier_portadora_1.png)   | ![sinal 2](media/fourie_portadora2.png)| 

---

**Fourier dos sinais modulados**

|          Sinal 1                            |        Sinal 2       |
|-----------------------------                |--------------------------|
| ![sinal 1](media/fourier_modulada_1.png)    | ![sinal 2](media/fourier_modulada_2.png)| 

---

**Fourier da soma dos sinais modulados**

![sinal 1](media/fourier_soma_moduladas.png)

---

### Receptor 

**Sinal recebido no tempo**

![sinal 1](media/sinal_recebido_tempo.png)

---

**Fourier do sinal recebido**

![sinal 1](media/fourier_sinal_recebido.png)

---

**Sinal recebido demodulado no tempo**

|          Sinal 1                                |        Sinal 2       |
|-----------------------------                    |--------------------------|
| ![sinal 1](media/sinal_tempo_demodulado1.png)   | ![sinal 2](media/sinal_tempo_demodulado2.png)| 

---

**Fourier do sinal recebido**

|          Sinal 1                                |        Sinal 2       |
|-----------------------------                    |--------------------------|
| ![sinal 1](media/fourier_audio_filtrado1.png)   | ![sinal 2](media/fourier_audio_filtrado2.png)| 

## Resultados

Os sinais ficaram bem parecidos com os sinais enviados, porém os áudios ficaram um pouco mais "robotizados" e houve uma mínima perda de qualidade.