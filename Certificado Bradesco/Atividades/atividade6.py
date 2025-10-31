numeros = []

print("Digite números POSITIVOS (um por vez).")
print("Para parar, digite um número NEGATIVO.\n")

while True:
    try:
        entrada = float(input("Digite um número positivo (ou negativo para parar): "))
        
        if entrada < 0:
            print("Número negativo detectado. Parando...")
            break
        
        num = int(entrada)
        
        if num != entrada:
            print(f"Aviso: número decimal ({entrada}) truncado para {num}.")
        
        if num in numeros:
            print(f"Número {num} já foi digitado. Ignorando repetição.")
        else:
            numeros.append(num)
            print(f"Número {num} adicionado.")
            
    except ValueError:
        print("Erro: digite um número válido.")

if len(numeros) == 0:
    print("\nNenhum número positivo foi digitado.")
else:
    print(f"\nLista final (sem repetições): {numeros}")
    print(f"Total de números únicos: {len(numeros)}")