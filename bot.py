import os
import requests
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

client = TradingClient(API_KEY, SECRET_KEY, paper=True)

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

def main():
    send_message("🤖 Bot iniciado correctamente.")
    # Ejemplo: compra simulada de una acción de AAPL
    market_order_data = MarketOrderRequest(
        symbol="AAPL",
        qty=1,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY
    )
    client.submit_order(order_data=market_order_data)
    send_message("✅ Orden de compra simulada enviada para AAPL.")

if __name__ == "__main__":
    main()
