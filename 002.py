import pandas as pd

df = pd.read_csv('VITOR HUGO PEREIRA RODRIGUES - Automobile_data - VITOR HUGO PEREIRA RODRIGUES - Automobile_data.csv')
df_cleaned = df.dropna(subset=['price']).drop_duplicates().reset_index(drop=True)

combined = pd.concat([df_cleaned.head(5), df_cleaned.tail(5)])
print(combined)