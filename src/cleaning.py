import pandas as pd
import numpy as np
from datetime import datetime


file_path = 'data/Online_Retail.xlsx'
xls_data = pd.read_excel(file_path)

def load_data(file_path):
    file_path = 'data/Online_Retail.xlsx'
    xls = pd.read_excel(file_path)

    xls_data = xls.sort_values(by='InvoiceDate').reset_index(drop=True)

    return xls_data.shape, xls_data.head(5)

# Checking for missing values to get a sense of the data.

# Some price data is negative, implying debt, while quantities for certain items are also negative implying outflow.

# Some CustomerIDs are missing 

# Some items have been mislabeled as other items

# Entries in the Description column are in combination upper- and lower-case, while item names are entirely in upper-case 

def empty_values(file_path):
    file_path = 'data/Online_Retail.xlsx'
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

# Filling empty Customer IDs with -1
def fill_missing_cust_id(file_path):
    file_path = 'data/Online_Retail.xlsx'
    xls_data = pd.read_excel(file_path)
    prior_missing_cust_ids= xls_data['CustomerID'].isnull().sum()
    xls_data['CustomerID'] = xls_data['CustomerID'].fillna(-1)

    post_missing_cust_ids = xls_data['CustomerID'].isnull().sum()

    return prior_missing_cust_ids, post_missing_cust_ids








    


