from datetime import datetime

from binance.spot import Spot

client = Spot()


# Get BTCUSDT last 1m candlestick data and store it as csv
def get_klines_data():
    btc_data = client.klines("BTCUSDT", "1m")
    # get the year,month,day of the first candlestick,which is the name of the csv file
    first_candlestick = datetime.fromtimestamp(btc_data[0][0] / 1000)
    name = first_candlestick.strftime("%Y-%m-%d")
    # parse json data to csv
    with open("data/klines/" + name + ".csv", "w") as f:
        f.write("开盘时间,开盘价,最高价,最低价,收盘价,成交量,收盘时间,成交额,成交笔数,主动买入成交量,主动买入成交额\n")
        for candlestick in btc_data:
            # convert ms to date time
            candlestick[0] = datetime.fromtimestamp(candlestick[0] / 1000)
            f.write(
                f"{candlestick[0]},{candlestick[1]},{candlestick[2]},{candlestick[3]},{candlestick[4]},{candlestick[5]},{candlestick[6]},{candlestick[7]},{candlestick[8]},{candlestick[9]},{candlestick[10]}\n"
            )
    return 1
