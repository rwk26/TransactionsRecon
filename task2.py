import pandas as pd
import re
df = pd.read_csv('Task2.csv')
def extract_transaction_id(text):
    match = re.search(r'539\d{9}', text)
    if match:
        return match.group(0)
    return None
df['Transaction ID'] = df['MescrSptSoT '].apply(extract_transaction_id)
print(df[['MescrSptSoT ', 'Transaction ID']].head())
df.to_csv('UpdatedBankStatement.csv', index=False)