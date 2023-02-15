# `Arithmetic operations on binary numbers`

![This is an image](https://img.shields.io/badge/Python-100%25-orange)
![This is an image](https://img.shields.io/badge/version-0.1-lightblue)

Investigate the algorithms used in microprocessors for multiplication and division of integers and approaches to working with real numbers

## Theory

Column multiplication is the process of addition + shift. At the same time, the result contains twice as many bits. The analysis of bits is done from right to left, after each step you need to shift the partial result to the left by one position. At each step, you need to add the 1st multiplier, if the current bit of the 2nd multiplier is equal to 1.


<p align="center"><img src="https://hardzone.es/app/uploads-hardzone.es/2021/06/Multiplicacion-Division-ALU-multiplos-2.jpg" /></p>
<p align="center">Algorithm of multiplication in a column</p>
