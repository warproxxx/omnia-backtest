import os
import requests
import pandas as pd

def download_file(name):
    try:
        print(name)
        op_file = 'data/{}'.format(name)

        if not os.path.isfile(op_file):

            for url in ["https://data.binance.vision/data/futures/um/daily/aggTrades/BTCUSDT/BTCUSDT-aggTrades-{}.zip".format(name), "https://data.binance.vision/data/spot/daily/aggTrades/BTCUSDT/BTCUSDT-aggTrades-{}.zip".format(name)]:
                r = requests.get(url)

                if not(os.path.isdir("data/")):
                    os.mkdir("data/")

                if "futures" in url:
                    fname = "futures_" + name
                else:
                    fname = "spot_" + name

                with open('data/{}.zip'.format(fname), 'wb') as f:
                    f.write(r.content)
    except Exception as e:
        print("Error: {} in {}".format(str(e), name))


if __name__ == "__main__":
    dates = pd.date_range("2023-02-01", "2023-02-03")
    for date in dates:
        curr = date.strftime('%Y-%m-%d')
        print(curr)
        download_file(curr)

