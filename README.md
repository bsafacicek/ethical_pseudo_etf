
# Ethical Pseudo ETF

Instal the following dependencies.

```bash
pip3 install yfinance
pip3 install pandas-datareader
```

## Reading stock positions.

I keep my stock positions in a Google sheet but reading it via libraries like gspread is an overkill as they require to create a Cloud project. Instead, I download the Google sheet into a local csv file.
