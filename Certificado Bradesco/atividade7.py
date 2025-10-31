pessoas = []

print("Digite a altura (em metros) e o peso (em kg) de 5 pessoas.\n")

for i in range(1, 6):
    print(f"--- Pessoa {i} ---")
    while True:
        try:
            altura = float(input(f"  Altura (ex: 1.75): "))
            if altura <= 0:
                print("Erro: altura deve ser positiva.")
                continue
            break
        except ValueError:
            print("Erro: digite um número válido para altura.")
    
    while True:
        try:
            peso = float(input(f"  Peso (ex: 70.5): "))
            if peso <= 0:
                print("Erro: peso deve ser positivo.")
                continue
            break
        except ValueError:
            print("Erro: digite um número válido para peso.")
    
    pessoas.append((altura, peso))

duplicadas = False
vistos = set()  

print("\n" + "="*50)
print("RESULTADO DA VERIFICAÇÃO:")
print("="*50)

for i, (alt, pes) in enumerate(pessoas, 1):
    combinacao = (alt, pes)
    if combinacao in vistos:
        print(f"ENCONTRADO! Pessoa {i} tem os mesmos dados que outra pessoa:")
        print(f"   → Altura: {alt:.2f}m, Peso: {pes:.2f}kg")
        duplicadas = True
    else:
        vistos.add(combinacao)
    print(f"Pessoa {i}: Altura = {alt:.2f}m, Peso = {pes:.2f}kg")

if not duplicadas:
    print("\nNenhuma pessoa tem a mesma altura e o mesmo peso.")
else:
    print("\nPelo menos duas pessoas têm altura e peso iguais.")