# Ethical Pseudo ETF

## How to use?

### Stock

```bash
python3 stock.py --money=20000
```

returns integer stock counts to buy given investment money and existing stock positions.

### Crypto

```bash
python3 crypto.py --money=2000
```

returns US dollar amount for each coin. This is enough information as I use Robinhood for crypto investing which supports fractional share buying unlike Chase I use as the stock broakage account.


## What do I mean by "Pseudo ETF"?

I call this portfolio "Pseudo ETF" as I only trade integer stocks (no fractional share) and I do not sell stocks to match the index. So, I never match the perfect index but I buy towards it.

## What do I mean by "Ethical ETF"?

I try to avoid buying stocks from companies in sectors that do not match my ethical values. Even tough there are ETFs out there matching my ethics, the commision rates are typically at least 10 times more than that of VOO of Vanguard making them less attractive.

I also do not want to buy individual stocks without an automated criterion to avoid emotional trading. This repo is to standardize my stock selling strategy as I have more money to invest in.

## Investment Strategy

Goal is to buy stocks to get closer to the equilibrium point which is a market-cap weighted index of the stocks in the index.

Let say I have invested X USD so far to a subset of stocks in the index. Now, I have additional Y USD that I want to invest.

First, I compute the stock mapping for X+Y USD by computing the market cap of each company.

As an example it will return sth like the following, {'NVDA': 3, 'AAPL': 4}.

But, say my current positions are {'NVDA': 4, 'AAPL': 0}. This means I had more NVDA stocks than I supposed to.

Ideally, I buy "-1" NVDA and "4" Apple, stocks_to_buy={'NVDA': -1, 'AAPL': 4}.

But, this strategy involves no selling, so I won't be able to buy all AAPL stocks I need to.

To compute how many of them I can actually buy, I will sum over all stocks that are positive in stocks_to_buy. Let us call this sum Z>Y.

Then I multiply all the stocks to be bought (stocks_to_buy) with Y/Z.

## Positions Sheet

This is a Google sheet of "ethical" companies that I gathered mostly from top-10 publicly announced companies of the ETFs.

I keep my index tickers in a Google sheet but reading it via libraries like [gspread](https://docs.gspread.org/en/v6.0.0/) is an overkill as they require to create a Cloud project. Instead, I download the Google sheet into another local csv file.

## Reading stock positions.

I use a Chase brokage account. I download my positions from "Investments -> Positions -> Things you can do -> Export as -> CSV".

## Requirements

Install the following dependencies.

```bash
pip3 install yfinance
pip3 install pandas-datareader
pip3 install cryptocmd
```
