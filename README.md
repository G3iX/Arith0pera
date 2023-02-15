# `Arithmetic operations on binary numbers`

![This is an image](https://img.shields.io/badge/Python-100%25-orange)
![This is an image](https://img.shields.io/badge/version-0.1-lightblue)

Investigate the algorithms used in microprocessors for multiplication and division of integers and approaches to working with real numbers

## Theory

Column multiplication is the process of addition + shift. At the same time, the result contains twice as many bits. The analysis of bits is done from right to left, after each step you need to shift the partial result to the left by one position. At each step, you need to add the 1st multiplier, if the current bit of the 2nd multiplier is equal to 1.


<p align="center" alt="alt text"><img src="https://hardzone.es/app/uploads-hardzone.es/2021/06/Multiplicacion-Division-ALU-multiplos-2.jpg" width="500" height="350" /></p>
<p align="center">Algorithm of multiplication in a column</p>

Multiplication based on the shift of the result to the right is faster than addition, because instead of addition, the operation of shifting the result to the right is used at each subsequent step

<p align="center" alt="alt text"><img src="![image](https://user-images.githubusercontent.com/86187704/219133954-2b526295-b925-4001-8ec9-58c52ad4ef88.png)
" width="500" height="350" /></p>
<p align="center">Multiplication algorithm based on shifting the result to the right</p>
