bandas = {
    "Gangrena Gasosa": [
        {"álbum": "Gente Ruim Só Manda Lembrança Pra Quem Não Presta", "ano": 2019},
        {"álbum": "Se Deus É 10, Satanás É 666", "ano": 1999},
        {"álbum": "Welcome to the Macumba", "ano": 1993}
    ],
    "Rogério Skylab": [
        {"álbum": "Nas Portas do Cu", "ano": 2023},
        {"álbum": "Crítica da Faculdade do Cu", "ano": 2021},
        {"álbum": "Cosmos", "ano": 2019}
    ],
    "Garotos Podres": [
        {"álbum": "Canções para Ninar", "ano": 2003},
        {"álbum": "Com a Corda Toda", "ano": 1997},
        {"álbum": "Rock de Subúrbio", "ano": 1995}
    ],
    "Massacration": [
        {"álbum": "Live Metal Espancation", "ano": 2017},
        {"álbum": "Good Blood Headbanguers", "ano": 2009},
        {"álbum": "Gates of Metal Fried Chicken of Death", "ano": 2005}
    ],
    "Raimundos": [
        {"álbum": "Cantigas de Roda", "ano": 2014},
        {"álbum": "Roda Viva", "ano": 2006},
        {"álbum": "Éramos 4", "ano": 2001}
    ]
}

album_mais_antigo = None
ano_mais_antigo = float('inf')
banda_mais_antiga = ""

for banda, albuns in bandas.items():
    for album in albuns:
        if album["ano"] < ano_mais_antigo:
            ano_mais_antigo = album["ano"]
            album_mais_antigo = album["álbum"]
            banda_mais_antiga = banda

maior_intervalo = 0
banda_maior_intervalo = ""

for banda, albuns in bandas.items():
    if len(albuns) < 2:
        continue
    anos = [a["ano"] for a in albuns]
    intervalo = max(anos) - min(anos)
    if intervalo > maior_intervalo:
        maior_intervalo = intervalo
        banda_maior_intervalo = banda

todos_albuns = []
for banda, albuns in bandas.items():
    for album in albuns:
        todos_albuns.append({
            "banda": banda,
            "álbum": album["álbum"],
            "ano": album["ano"]
        })

todos_albuns.sort(key=lambda x: x["ano"], reverse=True)

print("="*70)
print("RELATÓRIO DE BANDAS E ÁLBUNS")
print("="*70)

print(f"1. Álbum mais antigo:")
print(f"   → '{album_mais_antigo}' - {banda_mais_antiga} ({ano_mais_antigo})\n")

print(f"2. Banda com maior intervalo entre álbuns:")
print(f"   → {banda_maior_intervalo} ({maior_intervalo} anos)\n")

print(f"3. Todos os álbuns (do mais novo para o mais antigo):")
print("-" * 70)
for item in todos_albuns:
    print(f"   {item['ano']} | {item['banda']:20} → {item['álbum']}")