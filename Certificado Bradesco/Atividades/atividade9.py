alunos = {
    "Alice": 8.5,
    "Bruno": 7.8,
    "Carla": 9.2,
    "Diego": 6.9,
    "Eva": 8.0,
    "Fernando": 7.5,
    "Gabriela": 9.0,
    "Henrique": 6.7,
    "Isabela": 8.3,
    "João": 7.2
}

total_alunos = len(alunos)

tem_nota_zero = 0 in alunos.values()

menor_nota = min(alunos.values())

maior_nota = max(alunos.values())

print("="*50)
print("RELATÓRIO DAS NOTAS")
print("="*50)

print(f"1. Quantidade de alunos: {total_alunos}")

if tem_nota_zero:
    print("2. Sim, alguém tirou nota zero.")
else:
    print("2. Não, ninguém tirou nota zero.")

print(f"3. Menor nota: {menor_nota}")
print(f"4. Maior nota: {maior_nota}")