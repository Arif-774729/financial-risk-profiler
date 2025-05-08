import pandas as pd
import sqlite3

df = pd.read_csv('generated_data.csv')


conn = sqlite3.connect('financial_data.db')


df.to_sql('user_data', conn, if_exists='replace', index=False)

conn.close()
print("✅ Data loaded into SQLite database successfully!")
