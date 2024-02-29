
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

I keep my stock positions in a Google sheet but reading it via libraries like gspread is an overkill as they require to create a Cloud project. Instead, I download the Google sheet into a local csv file.

## Requirements

Install the following dependencies.

```bash
pip3 install yfinance
pip3 install pandas-datareader
```
