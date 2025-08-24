
from src.csv_handler.csv_handler import CsvHandler

def test_csv_handler_initialization():
    path = "data/data.csv"
    csv_handler = CsvHandler(path)
    assert csv_handler.csv_path == path
    assert not csv_handler.csv_df.empty
