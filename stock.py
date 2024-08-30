"""Computes number of stocks to buy."""

import argparse

import utils

parser = argparse.ArgumentParser()

parser.add_argument('--money',
                    type=float,
                    required=True,
                    help='Additional money to invest.')

if __name__ == '__main__':

  args = parser.parse_args()
  utils.stock_to_buy(args.money)
