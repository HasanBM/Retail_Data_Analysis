import pytest
from src.cleaning import load_data, fill_missing_cust_id

@pytest.mark.it("checks whether the data has the necessary number of columns and is non-empty")
def test_load_data():
    file_path = 'data/Online_Retail.xlsx'
    data_shape, data_head, data_info = load_data(file_path)
    assert data_shape[1] == 8
    assert data_head.empty == False

@pytest.mark.it("checks whether the missing Customer IDs have been filled")
def test_missing_IDs():
    file_path = 'data/Online_Retail.xlsx'
    prior_ids, post_ids = fill_missing_cust_id(file_path)
    assert prior_ids > 0
    assert post_ids == 0

