from typing import Any, Union
import yfinance as yf
from pandas import read_csv


def read_positions(path: str = '../data/stocks_2024 - stocks.csv'):
    """Reads positions from a csv file."""
    data = read_csv(path)
    nyse_list = data['NYSE']
    # To access, full names use data['NAME'].
    position_list = data['POSITIONS']
    return {nyse_list[i]: position_list[i] for i in range(len(nyse_list))}


POSITIONS = read_positions()


def print_red(text):
    print("\033[91m {}\033[00m" .format(text))


# Market cap of 500th company from https://companiesmarketcap.com/page/5/
MIN_MARKET_CAP = 38.84 * 1e9


def get_stock_price(stock_name: str) -> float:
    try:
        return yf.Ticker(stock_name).info['previousClose']
    except:
        print(f'stock_name={stock_name}')
        import pdb
        pdb.set_trace()


def sort_dict(d: dict[Any, Union[float, int]]) -> dict[Any, Union[float, int]]:
    """Reverse sorts based on values."""
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))


def print_dict(x: dict[str, float]) -> None:
    """Prints with 1 precision."""
    print({key: f'{value : .1f}' for key, value in x.items()})


def compute_total_market_cap_and_position() -> tuple[float, float]:
    total_quantity = 0
    total_position = 0.0
    dividend_yields = {}
    market_caps = {}
    for i, (stock_name, quantity) in enumerate(POSITIONS.items()):
        info = yf.Ticker(stock_name).info

        if i == 0:
            print(f'info={info.keys()}')

        # Note that dividendRate refers to dollar amount so it is a misnomer.
        dividend_yield = info.get('dividendYield', 0.0)
        dividend_yields[stock_name] = dividend_yield

        market_caps[stock_name] = info['marketCap']

        if info['marketCap'] < MIN_MARKET_CAP:
            print(
                f'{stock_name} has market cap of {market_caps[stock_name] / 1e9 : .2f}. So, likely not in SP500.')

        total_quantity += quantity
        total_position += quantity * get_stock_price(stock_name)

    total_market_cap = sum(market_caps.values())
    print(f'Total market cap = {total_market_cap * 1.0 / 1e12 : .2f}T.')
    print('To give an idea, SP500 market cap is 42T.')
    print(f'Number of companies = {len(POSITIONS)}')
    print(f'Total quantity = {total_quantity}')
    print(f'Total value = {total_position/1000 : .2f} K')

    dividend_yields = sort_dict(dividend_yields)
    dividend_yields = {key: f'{value * 100.0 : .2f}%' for key,
                       value in dividend_yields.items()}
    print(f'Dividend yields = {dividend_yields}')

    return total_market_cap, total_position