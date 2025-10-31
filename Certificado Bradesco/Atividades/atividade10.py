animes = {
    "Naruto": 220,
    "Jujutsu Kaisen": 47,
    "Dragon Ball Z": 291,
    "Death Note": 37,
    "Fullmetal Alchemist": 64,
    "Evangelion": 26,
    "Berserk": 25,
    "Code Geass": 50,
    "Akame ga Kill!": 24,
    "Elfen Lied": 13
}

total_episodios = sum(animes.values())

percentuais = {}
for nome, episodios in animes.items():
    percentual = (episodios / total_episodios) * 100
    percentuais[nome] = percentual

animes_ordenados = sorted(percentuais.items(), key=lambda x: x[1], reverse=True)

print("="*60)
print("RELATÓRIO DE ANIME POR EPISÓDIOS")
print("="*60)

print(f"1. Total de episódios (todos os animes): {total_episodios}")
print("\n2. Percentual de episódios por anime (ordem decrescente):")
print("-" * 60)

for nome, perc in animes_ordenados:
    print(f"{nome:20} → {perc:6.2f}%")