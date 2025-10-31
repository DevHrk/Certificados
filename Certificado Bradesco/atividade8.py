pessoas = []

print("Digite o NOME e a IDADE das pessoas.")
print("Para parar, deixe o NOME em branco (apenas pressione Enter).\n")

while True:
    nome = input("Nome: ").strip()
    
    if nome == "":
        print("Nome vazio detectado. Parando...\n")
        break
    
    while True:
        try:
            idade = int(input(f"Idade de {nome}: "))
            if idade < 0:
                print("Erro: idade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Erro: digite um número inteiro válido para a idade.")
    
    pessoas.append((nome, idade))
    print(f"{nome} (idade {idade}) adicionado(a).\n")

if len(pessoas) == 0:
    print("Nenhuma pessoa foi cadastrada.")
else:
    pessoa_mais_velha = max(pessoas, key=lambda p: p[1])
    nome_mais_velho, idade_mais_velha = pessoa_mais_velha
    
    print("="*50)
    print("RESULTADO:")
    print("="*50)
    print(f"Todas as pessoas cadastradas:")
    for nome, idade in pessoas:
        print(f"  → {nome}: {idade} ano(s)")
    
    print(f"\nA pessoa mais velha é: {nome_mais_velho}")
    print(f"Idade: {idade_mais_velha} ano(s)")