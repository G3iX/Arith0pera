# `Arithmetic operations on binary numbers`

![This is an image](https://img.shields.io/badge/Python-100%25-orange)
![This is an image](https://img.shields.io/badge/version-0.1-lightblue)

Investigate the algorithms used in microprocessors for multiplication and division of integers and approaches to working with real numbers

## Theory

Column multiplication is the process of addition + shift. At the same time, the result contains twice as many bits. The analysis of bits is done from right to left, after each step you need to shift the partial result to the left by one position. At each step, you need to add the 1st multiplier, if the current bit of the 2nd multiplier is equal to 1.


<p align="center" alt="alt text"><img src="https://hardzone.es/app/uploads-hardzone.es/2021/06/Multiplicacion-Division-ALU-multiplos-2.jpg" width="500" height="350" /></p>
<p align="center">Algorithm of multiplication in a column</p>

Multiplication based on the shift of the result to the right is faster than addition, because instead of addition, the operation of shifting the result to the right is used at each subsequent step

<p align="center" alt="alt text"><img src="https://user-images.githubusercontent.com/86187704/219133954-2b526295-b925-4001-8ec9-58c52ad4ef88.png" width="500" height="350" /></p>
<p align="center">Multiplication algorithm based on shifting the result to the right</p>

Multiplier in the right part of the register - the LSB of the multiplier is available, a single register is used to shift to the right 32 times, the more units - the more you need to add
<p align="center" alt="alt text"><img src="https://user-images.githubusercontent.com/86187704/219134758-d20b1623-0de9-414b-9234-028b705eb58b.png" width="500" height="350" /></p>
<p align="center">The multiplication algorithm is the multiplier in the right part of the register</p>

Booth's algorithm is a multiplication of binary numbers, where the speed of operation is the main aspect, the engineering task of which is to reduce the number of additions. The algorithm also works for signed numbers. The key idea is to convert the addition of a sequence of units into 1 addition and 1 subtraction

## `Booth's algorithm`:

* Starting from LSB Multiplier (2nd multiplier), 2 bits are analyzed
  - Add 0 to the right before starting
* **00** - do nothing
* **10** – subtract the *Multiplicand* (1st multiplier) from the *Product*
  - The beginning of the unit sequence
* **11** - do nothing
  - The middle of the unit sequence
* **01** – add Multiplicand to Product
  - The end of the unit sequence
* Move the resulting case (Product) to the right

<p align="center" alt="alt text"><img src="https://user-images.githubusercontent.com/86187704/219134252-461d359b-1806-4f0a-a1b2-13d23fd25d58.png" width="500" height="550" /></p>
<p align="center">Booth's multiplication algorithm</p>

## `Column division`

> *Dividend* = *Quotient* * *Divisor* + *Remainder*

On each step of the algorithm:
* Shifting the Divisor to the right and comparing it to *Dividend*
* If the *Divisor* is larger, the next bit of *Quotient* = 0
* If *Divisor* is less - subtract, the next bit of *Quotient* = 1

<p align="center" alt="alt text"><img src="https://user-images.githubusercontent.com/86187704/219138767-feaefc54-d6ac-4a6b-8bf2-8484c45f878e.png" width="500" height="350" /></p>
<p align="center">Column division</p>

## `IEEE 754`

IEEE 754 is a widely used floating-point number representation format standard used in both software implementations of arithmetic operations and many hardware (CPU and FPU) implementations. Many compiler programming languages use this standard to store numbers and perform mathematical operations on them

This standard defines:
* Floating-point binary and decimal data formats for data exchange and data exchange
* Addition, subtraction, multiplication, division
* Convert between integer and floating point formats
* Exceptions in floating-point operations and their handling, including non-numeric data

The standard of real number:
* 1 bit - sign
* 8 bits – the exponent
* 23 bits - mantissa
