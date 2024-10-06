import pandas as pd
import numpy as np


file_path = 'data/Online_Retail.xlsx'
xls_data = pd.read_excel(file_path)

xls_data = xls_data.sort_values(by='InvoiceDate').reset_index(drop=True)

print(xls_data.head())
print(xls_data.info())
print(xls_data.describe())

# Checking for missing values getting a sense of the data.

# Some price data is negative, implying debt, while quantities for certain items are also negative implying outflow.

# Some CustomerIDs are missing 

# Some items have been mislabeled as other items

# Entries in the Description column are in combination upper- and lower-case, while item names are entirely in upper-case 