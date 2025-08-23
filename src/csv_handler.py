import pandas as pd
import yfinance as yf


class CsvHandler:
    def __init__(self, csv_path):
        self.csv_path = csv_path
    
    def csv_reader(self):
        csv_df = pd.read_csv(self.csv_path)
        csv_df.columns = csv_df.columns.str.strip()
        return csv_df
    
    def csv_validator(self):
        csv_df = self.csv_reader()
        csv_df["date"] = pd.to_datetime(csv_df["date"])

        # Új oszlopok létrehozása
        csv_df["yahoo_min"] = None
        csv_df["yahoo_max"] = None

        for idx, row in csv_df.iterrows():
            ticker = row["Ticker"]
            date = row["date"]

            # Időtartomány ±3 nap
            start = (date - pd.Timedelta(days=3)).strftime("%Y-%m-%d")
            end = (date + pd.Timedelta(days=3)).strftime("%Y-%m-%d")

            try:
                data = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=True)

                if not data.empty:
                    # Min és max záróár lekérdezése
                    min_val = data["Close"].min()
                    max_val = data["Close"].max()

                    # Ha Series, akkor .iloc[0], különben csak sima float()
                    min_price = float(min_val.iloc[0]) if isinstance(min_val, pd.Series) else float(min_val)
                    max_price = float(max_val.iloc[0]) if isinstance(max_val, pd.Series) else float(max_val)

                    # Értékek kerekítése és mentése
                    csv_df.at[idx, "yahoo_min"] = round(min_price, 2)
                    csv_df.at[idx, "yahoo_max"] = round(max_price, 2)
                else:
                    csv_df.at[idx, "yahoo_min"] = "No data"
                    csv_df.at[idx, "yahoo_max"] = "No data"

            except Exception as e:
                csv_df.at[idx, "yahoo_min"] = f"Error: {e}"
                csv_df.at[idx, "yahoo_max"] = f"Error: {e}"

        # Csak a szükséges oszlopokat mutassuk
        print(csv_df[["Ticker", "date", "Action", "price", "yahoo_min", "yahoo_max"]])


if __name__ == "__main__":
    path = "data/data.csv"
    csv = CsvHandler(path)
    csv.csv_validator()


    

    
