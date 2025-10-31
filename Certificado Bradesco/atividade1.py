numeros = []

for i in range(5):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número inteiro: "))
            numeros.append(num)
            break  
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

print("A lista de números digitados é:", numeros)