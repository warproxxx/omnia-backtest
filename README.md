This repo contains the python scripts used to download historic BTCUSD spot and derivative data and the notebook used to simulate and backtest a market-making logic.

## Setup
Have Jupyter notebook installed. Then install the modules with the following:
>python3 -m pip install -r requirements.txt

Then run this to download the dataset:
>python3 get_data.py

This will download the historic spot and derivative BTCUSDT trades data from Binance used to run the simulation.

## Analysis
The .ipynb notebooks perform a simple backtest. The backtest shows that the performance is very similar to spot long of the underlying. But the efficiency is extremly of this logic is huge and there is no impermanent loss -- only market exposure to the LPs.

### Backtest 1:
The first backtest done on a 10 minute duration of BTCUSDT spot binance data does 28000$ in volume with a capital of 20000$ and max exposure set of half of that in a 10 minute perform. The performance looks similar to Bitcoin's

<img alt="" src="https://i.ibb.co/F5shrNj/image.png">

### Backtest 2:
The second backtest done on a 3 day duration of more than 20 million BTCUSDT spot binance data performs very similarly doing 10 Million $ in volume with a capital of 20000$ and max exposure set of half of that.

<img alt="" src="https://i.ibb.co/1sXTbwM/image.png">



### Notes
1) The backtest make a 0 fee assumption. But omnia-protocol takes zero fees for swap and is thus realistic.
2) This is a very simple strategy brushed up in a couple hour for a hackathon submission to show the potential. More complex and better ones can be created with enough effort
3) The protocol will under no condition receive similar volume as binance. Binance volume and trade direction is just used a reference for a realistic simulation