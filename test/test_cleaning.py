import pytest
from src.cleaning import load_data, empty_countries

@pytest.mark.it("checks whether the data has the necessary number of columns and is non-empty")
def test_load_data():
    file_path = 'data/Online_Retail.xlsx'
    df = load_data(file_path)
    assert df.shape[1] == 8
    assert len(df) > 0

@pytest.mark.it("checks whether there are any empty country values")
def test_empty_countries():
    file_path = 'data/Online_Retail.xlsx'
    empty_country_rows_len = empty_countries(file_path)
    assert empty_country_rows_len == 0
    