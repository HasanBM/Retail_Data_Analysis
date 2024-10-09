import pytest
import pandas as pd
import os

from src.cleaning import load_data, fill_missing_cust_id, drop_duplicates

@pytest.mark.it("checks whether the data has the necessary number of columns and is non-empty")
def test_load_data():
    file_path = '/Users/HM/Desktop/Code/FOIL_DA_Task-10-2024/data/Online_Retail.xlsx'
    data_shape, data_head, data_info = load_data(file_path)
    assert data_shape[1] == 8
    assert data_head.empty == False

@pytest.mark.it("checks whether the missing Customer IDs have been filled")
def test_missing_IDs():
    file_path = '/Users/HM/Desktop/Code/FOIL_DA_Task-10-2024/data/Online_Retail.xlsx'
    prior_ids, post_ids = fill_missing_cust_id(file_path)
    assert prior_ids > 0
    assert post_ids == 0

@pytest.mark.it("checks whether duplicates have been dropped")
def test_drop_duplicates():
    sample_data = {
        'InvoiceNo': ['536365', '536365', '536366', 'c536367', '536367'],
        'StockCode': ['71053', '71053', '85123A', '85049', '85049'],
        'Description': ['WHITE METAL LANTERN', 'WHITE METAL LANTERN', 
                        'WHITE HANGING HEART T-LIGHT HOLDER', 'RED WOOLLY HOTTIE WHITE HEART.',
                        'RED WOOLLY HOTTIE WHITE HEART.'],
        'Quantity': [6, 6, 6, 6, 6],
        'UnitPrice': [3.39, 3.39, 2.55, 7.65, 7.65],
        'CustomerID': [17850, 17850, 17850, 17850, 17850],
        'Country': ['United Kingdom'] * 5
    }

    df = pd.DataFrame(sample_data)
    test_file_path = '/Users/HM/Desktop/Code/FOIL_DA_Task-10-2024/data/test_data.xlsx'
    df.to_excel(test_file_path, index=False)

    clean_data = drop_duplicates(test_file_path)
    print(clean_data)
    
    assert clean_data.shape[0] == 4
    assert clean_data.duplicated().sum() == 0
    
    os.remove(test_file_path)