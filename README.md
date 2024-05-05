### Automated Trading Bot
<p>
This project is a trading bot designed to execute an automated strategy in the cryptocurrency market, specifically using the Binance exchange platform. The main purpose of the bot is to save time and effort for investors, as well as to eliminate the emotional factor in decision making, which can help reduce the risk associated with manual trading.
</p>
##Technologies Used

- Code Editor: **Visual Studio Code**;
- Programming Language: **Python**;
- Python Libraries:
	- **Python-Binance**: To interact with the Binance API.
	- **NumPy**: For numerical calculations and data analysis.

##Installation and Setup
**1.- Clone the Repository:**
```
git clone https://github.com/3stefani/BotTrading
```
**2.- Install dependencies:**
```
pip install python-binance numpy
```
**3.- Configure the Binance API:***
- Register an account on Binance if you don't have one already.
- Generate your API credentials from your Binance account.
- Copy and paste the API keys into the bot's configuration file.
**4.- Run the Bot:**
```
BotTrading.py
```

##Possible errors:
 If the bot does not run, check the following:
- Check your internet connection.
- Add the executable as an exception to the antivirus.
- If you get the following error from Binace API: APIError(code=-1021): Timestamp for
this request was 1000ms ahead of the servers time, you must then synchronize your server's clock
operating system with that of the internet.

## Trading  Strategy
The strategy implemented in this bot is based on long-term trends and moving averages. The BTC-USDT cryptocurrency pair is analyzed in real-time using the Binance API. The logic of the strategy is as follows:

If the market trend is bullish, the price of BTC is below the moving average, and there are no open trades, the bot will place a buy order.
If the above conditions are not met, the bot will exit the current trade and reanalyze the data.

## Flowchart


![](https://lh4.googleusercontent.com/dEQ-mm26DiqUGydAE8ZQ4dQQSrfgKKBrASPB1tMU7_Bnvy69XTFvskBXNhvBdGBGet87m7eZBo02hZaONOcDRuFAH8BQC0C7xrEp4ufY9ZF7BrYAg1f2GmeiJLKdpfhrTg=w1280)

## Thank you :smile:
