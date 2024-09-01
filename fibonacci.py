def pertence_fibonacci(numero):
    """"
    Verifica se um número pertence à sequência de Fibonacci.

    A sequência de Fibonacci é uma sequência de números onde cada número é a soma dos dois anteriores, começando por 0 e 1.
    Esta função determina se um dado número está presente nessa sequência.

    Parâmetros:
    numero (int): O número a ser verificado.

    Retorna:
    bool: Retorna True se o número estiver na sequência de Fibonacci, caso contrário, retorna False.

    Algoritmo:
    1. Inicializa os primeiros dois números da sequência de Fibonacci: 0 e 1.
    2. Itera gerando a sequência de Fibonacci até que o número atual seja maior ou igual ao número fornecido.
    3. Se o número atual for igual ao número fornecido, retorna True.
    4. Se o loop terminar sem encontrar o número, retorna False.
    """
    a, b = 0, 1

    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

while True:
    try:
        numero = int(input("Digite um número para verificarmos se ele pertence à sequência de Fibonacci: "))
        if pertence_fibonacci(numero):
            print(f'O número {numero} pertence à sequência de Fibonacci.')
        else:
            print(f'O número {numero} não pertence à sequência de Fibonacci.')
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
