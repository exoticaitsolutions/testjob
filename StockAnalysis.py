import os
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Create an output directory if it doesn't exist
output_dir = "/output"
os.makedirs(output_dir, exist_ok=True)

# Retrieve stock price data for Apple Inc. (AAPL) for the last 5 years
stock = yf.Ticker("AAPL")
stock_data = stock.history(period="5y")

# Save the stock data to a CSV file
csv_file_path = os.path.join(output_dir, "AAPL_5y_data.csv")
stock_data.to_csv(csv_file_path)

# Generate a summary of the stock price data
summary = {
    "Highest Close": stock_data['Close'].max(),
    "Lowest Close": stock_data['Close'].min(),
    "Average Close": stock_data['Close'].mean()
}

print("Summary of AAPL Stock Price Data for the Last 5 Years:")
print(summary)

# Plot the closing prices
plt.figure(figsize=(14, 7))
plt.plot(stock_data.index, stock_data['Close'], label='Close Price')
plt.title('Apple Inc. (AAPL) Stock Price Over the Last 5 Years')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(output_dir, "AAPL_5y_chart.png"))
plt.show()
