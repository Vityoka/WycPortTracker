import pandas as pd
import yfinance as yf


class CsvHandler:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.csv_df = self._read_csv()
        self._validate_csv()
    
    def get_csv_as_df(self):
        return self.csv_df

    def _read_csv(self):
        csv_df = pd.read_csv(self.csv_path)
        csv_df.columns = csv_df.columns.str.strip()
        return csv_df
    
    def _validate_csv(self):
        self.csv_df["date"] = pd.to_datetime(self.csv_df["date"])

        # Create new columns
        self.csv_df["yahoo_min"] = None
        self.csv_df["yahoo_max"] = None

        for idx, row in self.csv_df.iterrows():
            ticker = row["Ticker"]
            date = row["date"]

            # Time interval +/- 3 days
            start = (date - pd.Timedelta(days=3)).strftime("%Y-%m-%d")
            end = (date + pd.Timedelta(days=3)).strftime("%Y-%m-%d")

            try:
                ticker_price_history = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=True)

                if not ticker_price_history.empty:
                    # get min and max price
                    min_val = ticker_price_history["Close"].min()
                    max_val = ticker_price_history["Close"].max()


                    min_price = float(min_val.iloc[0]) if isinstance(min_val, pd.Series) else float(min_val)
                    max_price = float(max_val.iloc[0]) if isinstance(max_val, pd.Series) else float(max_val)

                    self.csv_df.at[idx, "yahoo_min"] = round(min_price, 2)
                    self.csv_df.at[idx, "yahoo_max"] = round(max_price, 2)
                else:
                    self.csv_df.at[idx, "yahoo_min"] = "No data"
                    self.csv_df.at[idx, "yahoo_max"] = "No data"

            except Exception as e:
                self.csv_df.at[idx, "yahoo_min"] = f"Error: {e}"
                self.csv_df.at[idx, "yahoo_max"] = f"Error: {e}"

        print(self.csv_df[["Ticker", "date", "Action", "price", "yahoo_min", "yahoo_max"]])


if __name__ == "__main__":
    path = "data/data.csv"
    csv = CsvHandler(path)



    

    
