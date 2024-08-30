"""Computes number of coins to buy."""

import utils

import argparse
import cryptocmd
from datetime import datetime


parser = argparse.ArgumentParser()

parser.add_argument('--money',
                    type=float,
                    required=True,
                    help='Additional money to invest.')

TICKERS = ['BTC',
           'ETH',
           'LINK',
           'AVAX',
           'XLM',
           'LTC',
           'BCH',
           'ETC',
           'XTZ',
           'UNI',
           ]

if __name__ == '__main__':
  args = parser.parse_args()
  now = datetime.now()
  today = f'{now.day}-{now.month}-{now.year}'
  print(f'today={today}')

  coin_cap = {}
  for ticker in TICKERS:
    scraper = cryptocmd.CmcScraper(coin_code=ticker,
                                   start_date='13-04-2024',
                                   end_date=today)
    headers, vals = scraper.get_data()
    assert len(vals) == 1, len(vals)
    for header, val in zip(headers, vals[0]):
      if header == 'Market Cap':
        print(f'Market Cap {ticker}: {val / 1e9 : .2f}')
        coin_cap[ticker] = val
      elif header == 'Close':
        print(f'Close {ticker}: {val : .2f}')

  total_cap = sum(coin_cap.values())
  print(f'total_cap: {total_cap / 1e12 : .2f}T')

  money_to_invest = {name: val * args.money /
                     total_cap for name, val in coin_cap.items()}
  money_to_invest = utils.sort_dict(money_to_invest)
  print({key: f'{value : .1f}' for key, value in money_to_invest.items()})
  total = sum(money_to_invest.values())
  print({key: f'{value/total*100 : .1f}' for key,
        value in money_to_invest.items()})
