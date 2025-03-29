num1 = float(input("Insira o primeiro número: "))
op = str(input("Escolha a operação:\n +(soma)\n - (subtração)\n * (multiplicação)\n / (divisão): "))
num2 = float(input("Insira o segundo número: "))

if op == "+":
    print(f"O resultado é: {num1 + num2}")
elif op == "-":
    print(f"O resultado é: {num1 - num2}")
elif op == "*":
    print(f"O resultado é: {num1 * num2}")
elif op == "/":
    print(f"O resultado é: {num1 / num2}")
else:
    print("Insira uma das operações válidas.")
