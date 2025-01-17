import ccxt


def getprice(symbol, exchange_id):
    symbol = symbol.upper()  # BTC/USDT, LTC/USDT, ETH/BTC, LTC/BTC
    exchange_id = exchange_id.lower()  # binance, #bitmex
    symbol_1 = symbol.split("/")
    exchange = getattr(ccxt, exchange_id)(
        {
            # https://github.com/ccxt/ccxt/wiki/Manual#rate-limit
            "enableRateLimit": True
        }
    )
    try:
        v_price = exchange.fetch_ticker(symbol)
        r_price = v_price["info"]["lastPrice"]
        return (
            "{:.2f} {}".format(float(r_price), symbol_1[1])
            if symbol_1[1] in ["USD", "USDT"]
            else "{:.8f} {}".format(float(r_price), symbol_1[1])
        )

    except (ccxt.ExchangeError, ccxt.NetworkError) as error:
        # add necessary handling or rethrow the exception
        return "Got an error", type(error).__name__, error.args
    raise


print(getprice("btc/usdt", "BINANCE"))
print(getprice("btc/usd", "BITMEX"))
