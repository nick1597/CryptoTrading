import os
import pandas as pd

# parse info from csv

def process_data():
    # get all csv files
    csv_files = os.listdir("data/klines")

    # get the trade data from every csv file with pandas
    trade_data = pd.DataFrame()
    for file in csv_files:
        df = pd.read_csv("data/klines/" + file)
        df["价差"] = df["收盘价"] - df["开盘价"]
        df["经流入资金"] = df["收盘价"] * df["成交量"]



