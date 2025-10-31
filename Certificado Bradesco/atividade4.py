notas = []

print("Digite as notas da prova (uma por vez).")
print("Para parar, digite um número negativo.\n")

while True:
    try:
        entrada = float(input("Digite uma nota (0 a 10) ou número negativo para parar: "))
        
        if entrada < 0:
            print("Entrada negativa detectada. Parando...")
            break
        
        if entrada > 10:
            print("Aviso: nota acima de 10. Será aceita, mas verifique se está correto.")
        
        notas.append(entrada)
        
    except ValueError:
        print("Erro: digite um número válido.")

if len(notas) == 0:
    print("\nNenhuma nota válida foi digitada.")
else:
    media = sum(notas) / len(notas)
    print(f"\nNotas digitadas: {notas}")
    print(f"Quantidade de notas: {len(notas)}")
    print(f"Média das notas: {media:.2f}")