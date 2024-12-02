import pandas as pd

df = pd.read_csv('sales_data_sample.csv', encoding='latin1')
df['ADDRESSLINE1'] =  df['ADDRESSLINE2'].fillna('') + ' ' + df['ADDRESSLINE1']
df['ADDRESSLINE1']=df['ADDRESSLINE1'].str.lstrip()
df.drop(columns=['ADDRESSLINE2'], inplace=True)
df['STATE']=df['STATE'].fillna('Unknown')
df['TERRITORY']=df['TERRITORY'].fillna('Unknown')
df['POSTALCODE']=df['POSTALCODE'].fillna('Unknown')
# **Step 2: Convert and Format Dates**
# Convert ORDERDATE to a standard datetime format
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
df.columns = df.columns.str.lower().str.replace(' ', '_')


df.to_csv('preprocessed_sales_data_sample.csv', index=False)