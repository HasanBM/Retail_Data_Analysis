import pandas as pd
from datetime import datetime


file_path = '/Users/HM/Desktop/Code/FOIL_DA_Task-10-2024/data/Online_Retail.xlsx'


def load_data(file_path):

    xls_data = pd.read_excel(file_path)

    xls_data = xls_data.sort_values(by='InvoiceDate').reset_index(drop=True)

    return xls_data.shape, xls_data.head(5), xls_data.info()

def empty_values(file_path):
    
    
    xls_data = pd.read_excel(file_path)

    cols = ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']
    
    empty_values_count = {}
    
    for col in cols:
        if xls_data[col].dtype == 'object':
            empty_values = xls_data[xls_data[col].isnull() | xls_data[col].str.strip() == ""]
        else:
            empty_values = xls_data[xls_data[col].isnull()]

        empty_values_count[col] = len(empty_values)

        if len(empty_values) > 0:
            print(f"Column {col} has {len(empty_values)} missing or empty values")
        else:
            print(f"No empty or missing values found in {col} column")
            
    return empty_values_count


def fill_missing_cust_id(file_path):

    xls_data = pd.read_excel(file_path)

    prior_missing_cust_ids= xls_data['CustomerID'].isnull().sum()

    xls_data['CustomerID'] = xls_data['CustomerID'].fillna(-1)

    post_missing_cust_ids = xls_data['CustomerID'].isnull().sum()

    return prior_missing_cust_ids, post_missing_cust_ids








    


