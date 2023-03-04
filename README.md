This repo contains the python scripts used to download historic BTCUSD spot and derivative data and the notebook used to simulate and backtest a market making logic.

## Setup
Have Jupyter notebook installed. Then install the modules with:
>python3 -m pip install -r requirements.txt

Then run this to download the dataset:
>python3 get_data.py

This will download the historic spot and derivative BTCUSDT trades data from binance used to run the simulation

## Notebook
The notebook uses backtrader module to perform backtest for market making logic that has been integrated in omnia-contracts.