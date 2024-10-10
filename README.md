# In XPlus_GPIO
Refactoring the XPlus TVBOX to access the GPIO

# Instalar o Armbian utilizando a ferramenta multitool
Link para o Tutorial: https://armbian.hosthatch.com/archive/rk322x-box/archive/
*No teste foi utilizada a imagem Armbian_24.2.5_Rk322x-box_bookworm

# TVBox  In XPlus
Especificações: SoC RK3329 (4 cores, ARM-V7), 2GB RAM, 8GB Flash)
![screenshot](inxplus.jpeg)

# RK3329 GPIO 
São 4 controladores GPIO totalizando 128 pinos. Alguns pinos tem utilização pre-definida para acesar dispositivos como flash, MMC, Wifi, HDMI etc. 
Baseado no trabalho do Instituto Federal de Goiás - Campus Goiânia, Aluno: Mateuss Morais Aguirre, orientado pelo Prof. Dr. Claudio Afonso Fleury, uma busca por pinos GPIO foi realizada. Para essa placa, foram identificados alguns pinos disponíveis, conforme tabela a seguir 

| GPIO          | Descrição     |
| ------------- | ------------- |
| 0   | GPIO0_A0/I2C0_SCL  |
| 1   | GPIO0_A1/I2C0_SDA  |
|41	| GPIO1_B1/UART1_TX/UART2_TX|
|42	| GPIO1_B2/UART1_RX/UART2_RX|
|96 |	GPIO3_A0/SDMMC1_CLKO |
|97 |	GPIO3_A1/SDMMC1_CMD |
|98 |	GPIO3_A2/SDMMC1_D0|
|99	|GPIO3_A3/SDMMC1_D1|
|100 |	GPIO3_A4/SDMMC1_D2|
|101 |	GPIO3_A4/SDMMC1_D2|
|102 |	GPIO3_A6/UART1_RTSN|
|103 |	GPIO3_A7/UART1_CTSN|

*As portas MMC1 podem ser utilizadas pois a placa utiliza somente o MMC0 que é o slot de cartão SD. A localização de cada um dos pinos é apresentada na figura abaixo.
![screenshot](Xplus_INschematic.png)

Para acessar o GPIO foram soldados fios esmaltados (utilizados para jumper). Os pinos GPIO 41 e 42 foram soldados diretamente pois a placa já contém os furos. Para facilitar o acesso aos demais pinos foi utilizado os furos existentes na placa, que foi identificado que não estão em uso (no PCB eles direcionam para um local com o diagrama de um chip, que nessa solução não foi utilizado).
Foi também identificado dois pinos GND e 3V3 para alimentação dos circuitos externos.


