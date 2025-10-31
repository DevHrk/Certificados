numeros = []

print("Digite 5 números inteiros (positivos ou negativos):")

for i in range(5):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número: "))
            numeros.append(num)
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

numeros_positivos = [num for num in numeros if num >= 0]

print("\nLista original:", numeros)
print("Lista sem números negativos:", numeros_positivos)