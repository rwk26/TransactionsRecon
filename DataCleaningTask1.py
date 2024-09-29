import pandas as pd
BankStatement= pd.read_csv('BankStatement.csv')
AdminNew= pd.read_csv('AdminNew.csv')
AdminOld= pd.read_csv('AdminOld.csv')
Declined= pd.read_csv('Declined.csv')
Declined=Declined[Declined['Provider (Declined Table)']=='SnowPay']
BankStatement.rename(columns={' Amount': 'BankAmount'}, inplace= True)
print(f'Bank Statement columns:{BankStatement.columns}')
print(f'Admin New columns:{AdminNew.columns}')
print(f'Admin Old columns:{AdminOld.columns}')
print(f'Declined transactions columns:{Declined.columns}')
print(BankStatement.shape)
#Starting merging bankstatement table on a common key ('Transaction ID') with rest of the tables
#df1: Bank + Admin new
df1= pd.merge(BankStatement, AdminNew, on= 'Transaction ID', how= 'left')
#df2: Bank + Admin new + Admin Old
df2= pd.merge(df1, AdminOld, on= 'Transaction ID', how= 'left')
df2.drop(columns=['Unnamed: 0_y','Currency_y','Unnamed: 0','Unnamed: 0_x'], inplace= True)
#Final merged table: Bank + Admin new + Admin Old + Declined 
FinalMergedTable= pd.merge(df2, Declined, on= 'Transaction ID', how= 'left')
def map_status(row):
    status_new = row['Status (Admin New Table)']
    status_old = row['Status (Admin Old Table)']
    status_declined = row['Status (Declined Table)']
    if any(s in ['Success', 'Success (updated)', 'Success (activated)'] for s in [status_new, status_old]) and status_declined == 'declined':
        return 'Success and Declined'
    elif status_new in ['Success', 'Success (updated)', 'Success (activated)'] or status_old in ['Success', 'Success (updated)', 'Success (activated)']:
        return 'Success'
    elif status_old in ['Not active'] and status_declined == 'declined':
        return 'Not active and declined'
    elif status_old in ['Not active']:
        return 'Not active'
    elif status_declined == 'declined':
        return 'Declined'
    elif pd.isna(status_new) and pd.isna(status_old) and pd.isna(status_declined):
        return 'non authorized transaction'
    else:
        return 'Unknown'
FinalMergedTable['Mapped Status'] = FinalMergedTable.apply(map_status, axis=1)
FinalMergedTable['BankVsAdminTablesDiff']= FinalMergedTable['BankAmount']-FinalMergedTable['Amount (Admin New Table)'] - FinalMergedTable['Amount (Admin Old Table)']
print(FinalMergedTable.columns)
print(FinalMergedTable.dtypes)
FinalMergedTable.to_csv('FinalMergedTable.csv')
print(FinalMergedTable['BankAmount'].sum())
