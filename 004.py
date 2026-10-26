import pandas as pd

# Ler o ficheiro CSV
df = pd.read_csv('VITOR HUGO PEREIRA RODRIGUES - Automobile_data - VITOR HUGO PEREIRA RODRIGUES - Automobile_data.csv')
# Agrupar por empresa e imprimir todos os detalhes
for company, group in df.groupby('company'):
    print("=" * 60)
    print(f"EMPRESA: {company.upper()}")
    print("=" * 60)
    print(group.to_string(index=False))
    print("\n")