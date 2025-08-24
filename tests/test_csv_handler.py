
from csv_handler.csv_handler import CsvHandler

def test_csv_handler_initialization():
    # ARRANGE
    path = "data/data.csv"
    # ACT
    csv_handler = CsvHandler(path)
    # ASSERT
    assert csv_handler.csv_path == path
    assert not csv_handler.csv_df.empty
