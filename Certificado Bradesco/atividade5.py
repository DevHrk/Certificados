pares = []
impares = []

print("Digite números POSITIVOS (um por vez).")
print("Para parar, digite um número NEGATIVO.\n")

while True:
    try:
        num = float(input("Digite um número positivo (ou negativo para parar): "))
        
        if num < 0:
            print("Número negativo detectado. Parando...")
            break
        
        if num != int(num):
            print("Aviso: número decimal detectado. Apenas a parte inteira será considerada.")
            num = int(num)  
        
        num = int(num)  
        
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
            
    except ValueError:
        print("Erro: digite um número válido.")

total_pares = len(pares)
total_impares = len(impares)
total_numeros = total_pares + total_impares

if total_numeros == 0:
    print("\nNenhum número positivo foi digitado.")
else:
    porcentagem_pares = (total_pares / total_numeros) * 100
    porcentagem_impares = (total_impares / total_numeros) * 100
    
    print(f"\nNúmeros digitados: {total_numeros}")
    print(f"   Pares: {pares} → {total_pares} ({porcentagem_pares:.1f}%)")
    print(f"   Ímpares: {impares} → {total_impares} ({porcentagem_impares:.1f}%)")