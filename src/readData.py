import pandas as pd
import yfinance as yf
import plotly.graph_objects as go


path = "data/data.csv"

df = pd.read_csv(path)

print(df.head())

# Define the stock symbol and date range
ticker = "AAPL"  # Apple Inc.
start_date = "2022-01-01"
end_date = "2023-12-31"

# Download historical data
data = yf.download("AAPL", start="2022-01-01", end="2023-12-31")

# Reset MultiIndex (in case it's set) and flatten
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)  # or [1] if needed

# Plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))

fig.update_layout(
    title="AAPL Stock Price",
    xaxis_title="Date",
    yaxis_title="Price (USD)"
)

fig.show()

