import os
import pandas as pd

# List files in the current working directory or check default locations
files = os.listdir('.')
print("Files:", files)

csv_file = None
for f in files:
    if f.endswith('.csv'):
        csv_file = f
        break

if csv_file:
    df = pd.read_csv(csv_file)
    print("--- HEAD ---")
    print(df.head(5))
    print("\n--- TAIL ---")
    print(df.tail(5))
    