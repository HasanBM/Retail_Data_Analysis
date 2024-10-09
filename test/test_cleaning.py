import pytest
from src.cleaning import load_data, empty_values


@pytest.mark.it("checks whether the data has the necessary number of columns and is non-empty")
def test_load_data():
    file_path = 'data/Online_Retail.xlsx'
    data_shape, data_head = load_data(file_path)
    assert data_shape[1] == 8
    assert data_head.empty == False

# We know from prior EDA that there are no empty cells in the "Country" column, and that there are empty cells in "CustomerID"

@pytest.mark.it("checks whether there are any empty cells in any columns")
def test_empty_values():
    file_path = 'data/Online_Retail.xlsx'
    empty_counts = empty_values(file_path)
    assert empty_counts['Country'] == 0
    assert empty_counts['CustomerID'] > 0

