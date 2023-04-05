import yfinance as yf

# Получаем данные об акции
stock = yf.Ticker("AAPL")

# Получаем цену закрытия за последние 30 дней
history = stock.history(period="30d")
close_prices = history["Close"]

# Выводим среднюю цену закрытия
average_price = close_prices.mean()
print(f"Average closing price over the last 30 days: {average_price}")
