import pytest
from src.cleaning import load_data

@pytest.mark.it("checks whether the data has the necessary number of columns and is non-empty")
def test_load_data():
    file_path = 'data/Online_Retail.xlsx'
    df = load_data(file_path)
    assert df.shape[1] == 8
    assert len(df) > 0

    