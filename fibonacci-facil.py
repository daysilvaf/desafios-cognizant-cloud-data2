DESAFIO
A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 
2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

ENTRADA
O arquivo de entrada contém um valor inteiro N (0 < N < 46).

SAÍDA
Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.

-----------------------------------------
| EXEMPLO DE ENTRADA | EXEMPLO DE SAÍDA | 
-----------------------------------------
|          5         |     0 1 1 2 3    |
-----------------------------------------

CÓDIGO

n = int(input())
fib_list = [0, 1]
n = n - 2
for i in range(n):
    next_fib = fib_list[-1] + fib_list[-2]
    fib_list.append(next_fib)

fib_string = ' '.join(map(str, fib_list))
print(fib_string)
