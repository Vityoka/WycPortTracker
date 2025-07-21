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
        dates = csv_df["date"]
        ticker = csv_df["Ticker"]
        csv_df["date"] = pd.to_datetime(csv_df["date"])

        # Create a new column for the actual fetched close price
        csv_df["yahoo_close"] = None

        # Loop over each row and fetch historical price
        for idx, row in csv_df.iterrows():
            ticker = row["Ticker"]
            date = row["date"]
            
            # Define date range (buffer around the date in case it's a weekend/holiday)
            start = (date - pd.Timedelta(days=3)).strftime("%Y-%m-%d")
            end = (date + pd.Timedelta(days=3)).strftime("%Y-%m-%d")
            
            # Download data
            try:
                data = yf.download(ticker, start=start, end=end)
                if not data.empty:
                    data.reset_index(inplace=True)
                    data["Date"] = pd.to_datetime(data["Date"])

                    # Find the closest date (e.g., if original was a weekend)
                    closest_row = data.iloc[(data["Date"] - date).abs().argsort()[:1]]
                    close_price = closest_row["Close"].values[0]
                    csv_df.at[idx, "yahoo_close"] = close_price
                else:
                    csv_df.at[idx, "yahoo_close"] = "No data"
            except Exception as e:
                csv_df.at[idx, "yahoo_close"] = f"Error: {e}"

        # Show final DataFrame with Yahoo prices
        print(csv_df)




if __name__ == "__main__":
    path = "data/data.csv"
    csv = CsvHandler(path)
    csv.csv_validator()


    

    
