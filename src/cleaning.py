import pandas as pd
from datetime import datetime


file_path = '/Users/HM/Desktop/Code/FOIL_DA_Task-10-2024/data/Online_Retail.xlsx'


def load_data(file_path):

    df = pd.read_excel(file_path)

    df = df.sort_values(by='InvoiceDate').reset_index(drop=True)

    return df.shape, df.head(5), df.info()


def empty_values(file_path):    
    df = pd.read_excel(file_path)

    cols = ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']
    
    empty_values_count = {}
    
    for col in cols:
        if df[col].dtype == 'object':
            empty_values = df[df[col].isnull() | (df[col].str.strip() == "")]
        else:
            empty_values = df[df[col].isnull()]

        empty_values_count[col] = len(empty_values)

        if len(empty_values) > 0:
            print(f"Column {col} has {len(empty_values)} missing or empty values")
        else:
            print(f"No empty or missing values found in {col} column")
            
    return empty_values_count


def fill_missing_cust_id(file_path):

    df = pd.read_excel(file_path)

    prior_missing_cust_ids= df['CustomerID'].isnull().sum()

    df['CustomerID'] = df['CustomerID'].fillna(-1)

    post_missing_cust_ids = df['CustomerID'].isnull().sum()

    return prior_missing_cust_ids, post_missing_cust_ids


def fill_missing_description(file_path):
    
    df = pd.read_excel(file_path)
    
    prior_missing_descriptions = df['Description'].isnull().sum()
    
    df['Description'] = df['Description'].fillna("Missing Description")
    
    post_missing_descriptions = df['Description'].isnull().sum()
    
    df.to_excel(file_path, index=False)
    return prior_missing_descriptions, post_missing_descriptions


def drop_duplicates(file_path):

    df = pd.read_excel(file_path)
    df = df.drop_duplicates()

    return df


def impute_unit_price(df):

    mask = df['UnitPrice'] <= 0
    for stock_code in df.loc[mask, 'StockCode'].unique():
        positive_prices = df[(df['StockCode'] == stock_code) & (df['UnitPrice'] > 0)]['UnitPrice']
        if not positive_prices.empty:
            mean_positive_price = positive_prices.mean()
            df.loc[(df['StockCode'] == stock_code) & mask, 'UnitPrice'] = mean_positive_price
            
    return df




    


