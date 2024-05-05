from binance.client import Client # We import the necessary libraries and connect to the Binace API.
from binance.enums import *
API_KEY = 'CW08CDlniRaMIZ5le6jG9ol73G4yKR8HXOtEhyptrewu3w4kuRwd3KMFgdGWPS1h' # Enter your API KEY from Binace.
API_SECRET = 'mDIZMeaFfogJpuQf4gZy19wCmNrs167QgKpazNlaxTzqp5K5CuhS9KTBLWiw1lXU'
import time
import numpy as np


cliente = Client(API_KEY, API_SECRET, tld='com')
moneda = 'BTCUSDT'
cantidadOrden = 0.00043 # Enter the quantity to purchase. This example is Amount to buy: $20 in Bitcoins, calculated based on the current price of Bitcoin.

#### This bot is with trend and long-term moving lines #### 
def tendencia():
    x = []
    y = []
    sum = 0
    ma48_i = 0

    resp = False

    klines = cliente.get_historical_klines(moneda, Client.KLINE_INTERVAL_15MINUTE, "12 hour ago UTC")


    if(len(klines) != 60):
        
        return False
    for i in range (24-60): # From line 24 to 60, 36 15-minute candles are 9 hours on average.

        for i in range (i-50,i): # We analyze from the index to line 50.
            sum = sum + float(klines[i][4]) # 4 is the closing price of the candle.
        ma48_i = '{:.0f}'.format(sum / 50)  # Divide the sum by the number of candles we have.
        sum = 0
        x.append(i)
        y.append(float(ma48_i))


    modelo = np.polyfit(x,y,1)
    if (modelo[0]>0) : # If the trend is bullish, greater than 0.
        resp = True
    return resp

def _ma48_():
    ma48_local = 0
    sum = 0


    klines = cliente.get_historical_klines(moneda, Client.KLINE_INTERVAL_15MINUTE, "12 hour ago UTC") # Return 12 hours divided into 15 minute intervals, which are 48 lines.


    if(len(klines)==48): 
        for i in range (0,48):
            sum = sum +float(klines[i][4]) # 4 is the closing price of the candle. Let it execute the sum of klines in its closures.


        ma48_local = sum / 48  # Divided by 48 to get the average.


    return ma48_local

while 1:
    ordenes = cliente.get_open_orders(symbol=moneda)
    print("Ordenes actuales abiertas: ") # If there are open orders, will not buy.
    print(ordenes)


    if(len(ordenes) !=0):
        print("Existen ordenes abiertas, no se compra")
        time.sleep(10)
        continue
   
    # We get the current price of the currency.

    list_of_tickers = cliente.get_all_tickers()
    for tick_2 in list_of_tickers:
        if tick_2['symbol'] == moneda:
            PrecioMoneda = float(tick_2['price'])
   

    ma48 =_ma48_()
    if (ma48 == 0): continue


    print("--------" + moneda + "--------")
    print(" Precio actual de MA48 " + str('{:.8f}'.format(ma48))) # The .8 is the number of decimals it returns, 8 decimals because the price of BTC is high.
    print(" Precio actual de la moneda " + str('{:.8f}'.format(PrecioMoneda)))
    print(" Precio a comprar " + str('{:.8f}'.format(ma48*0.995))) # We want to buy when the value is below the moving average.


    if (not tendencia()):
        print ("tendencia bajista, no se realizan ordenes de compra")

        time.sleep(10)
        continue
    else:
        print("tendencia alcista, comprar si no hay ordenes abiertas") # Because if I already have open orders, I don't want to buy again. You will operate on orders that are already open.
    

    if(PrecioMoneda > ma48*0.995):
        print("Comprando")


    orden = cliente.order_market_buy( # We open the order.
        symbol = moneda,
        quantity = cantidadOrden
    )

    time.sleep(5)

    # I place the OCO order (one cancels other).

    orderOCO = cliente.create_oco_order(
        symbol = moneda,
        side = SIDE_SELL,
        stoplimitPrice = str('{:.8f}'.format(PrecioMoneda*0.994)), # Price at which we are going to sell.
        stopLimitTimeInForce = TIME_IN_FORCE_GTC, # Make it synchronize with our schedule.
        quantity = cantidadOrden*0.999, # Binance charges a fee, otherwise it will give insufficient funds error.
        stopPrice = str('{:.8f}'.format(PrecioMoneda*0.995)),
        price = str('{:.8f}'.format(PrecioMoneda*0.995)),
    )


    time.sleep(20) # I put the robot to sleep because in theory it has opened an order, we let the market operate.


