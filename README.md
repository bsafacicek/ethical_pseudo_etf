
# Ethical Pseudo ETF

The main binary returns stocks to buy given investment money and existing stock positions.

## What do I mean by "Pseudo ETF"?

TODO

## What do I mean by "Ethical ETF"?

TODO

## Investment Strategy

No sell, no split share, ....

Markep-cap weighted.

TODO


## Sample Positions Sheet

TODO

## Reading stock positions.

I use a Chase brokage account. I download my positions from "Investments -> Positions -> Things you can do -> Export as -> CSV".

I keep my index tickers in a Google sheet but reading it via libraries like [gspread](https://docs.gspread.org/en/v6.0.0/) is an overkill as they require to create a Cloud project. Instead, I download the Google sheet into another local csv file.

## Requirements

Install the following dependencies.

```bash
pip3 install yfinance
pip3 install pandas-datareader
```
