from extract import df
import pandas as pd

df['TransactionID'] = df['TransactionID'].astype(int)
df['CustomerID'] = df['CustomerID'].astype(int)
df['ProductID'] = df['ProductID'].astype(int)
df['Quantity'] = df['Quantity'].astype(int)
df['Price'] = df['Price'].astype(float)
df['Discount'] = df['Discount'].astype(float)
df['CustomerAge'] = df['CustomerAge'].astype(int)
df['CustomerLoyaltyScore'] = df['CustomerLoyaltyScore'].astype(float)

# Fix date
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
df['TransactionDate'] = df['TransactionDate'].dt.strftime('%Y-%m-%dT%H:%M:%S')

sales_records = df.to_dict(orient='records')
print(sales_records[:2]) 