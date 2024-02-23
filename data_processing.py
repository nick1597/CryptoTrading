import os
import pandas as pd
from config_manager import ConfigManager
from datetime import datetime
from binance.spot import Spot

# Get the config
config = ConfigManager()
coin_list = config.get_config("coin_list")
client = Spot()


def check_data_folder(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return 1


# Get BTCUSDT last 1m candlestick data and store it as csv
def get_klines_data():
    for coin in coin_list:
        coin_data = client.klines(coin, "1m")
        first_candlestick = datetime.fromtimestamp(coin_data[0][0] / 1000)
        name = first_candlestick.strftime("%Y-%m-%d")
        check_data_folder("data/klines/" + coin + "/")
        with open("data/klines/" + coin + "/" + name + ".csv", "w") as f:
            f.write(
                "开盘时间,开盘价,最高价,最低价,收盘价,成交量,收盘时间,成交额,成交笔数,主动买入成交量,主动买入成交额\n")
            for candlestick in coin_data:
                candlestick[0] = datetime.fromtimestamp(candlestick[0] / 1000)
                f.write(
                    f"{candlestick[0]},{candlestick[1]},{candlestick[2]},{candlestick[3]},{candlestick[4]},{candlestick[5]},{candlestick[6]},{candlestick[7]},{candlestick[8]},{candlestick[9]},{candlestick[10]}\n"
                )
    return 1


def get_depth_data():
    for coin in coin_list:
        depth_data = client.depth(coin)
        first_candlestick = datetime.fromtimestamp(depth_data[0][0] / 1000)
        name = first_candlestick.strftime("%Y-%m-%d")
        check_data_folder("data/depth/" + coin + "/")
        with open("data/depth/" + coin + "/" + name + ".csv", "w") as f:
            f.write(
                "消息时间,撮合引擎时间,买单价格,买单数量,卖单价格,卖单数量\n")
            for depth in depth_data:
                data_time = depth['E']
                match_time = depth['T']
                buy_price = depth['bids'][0]
                buy_quantity = depth['bids'][1]
                sell_price = depth['asks'][0]
                sell_quantity = depth['asks'][1]
                f.write(
                    f"{data_time},{match_time},{buy_price},{buy_quantity},{sell_price},{sell_quantity}\n"
                )

    return 1

def process_data():
    # get all csv files
    csv_files = os.listdir("data/klines")

    # get the trade data from every csv file with pandas
    trade_data = pd.DataFrame()
    for file in csv_files:
        df = pd.read_csv("data/klines/" + file)
        df["价差"] = df["收盘价"] - df["开盘价"]
        df["经流入资金"] = df["收盘价"] * df["成交量"]
