"""Computes number of stocks to buy."""

import yfinance as yf
import utils


def stock_to_buy(money: float) -> None:
    total_market_cap, total_position = utils.compute_total_market_cap_and_position()
    total_money = total_position + money
    total_to_buy = 0.0
    ideal_buy = {}
    for stock_name, quantity in utils.POSITIONS.items():
        info = yf.Ticker(stock_name).info
        ratio = info['marketCap'] / total_market_cap
        money_on_stock = total_money * ratio

        stock_price = utils.get_stock_price(stock_name)

        to_buy = money_on_stock / stock_price - quantity
        if stock_name in ['GOOG', 'GOOGL']:
            # assuming that we always buy GOOG and GOOGL at the same quantity.
            to_buy /= 2

        # Since this require to sell some of the existing stocks,
        # will never be able to buy all positive to_buy's.
        if to_buy > 0:
            ideal_buy[stock_name] = to_buy  # math.ceil()

        # Remember that our strategy is to never sell and we will always have
        # some over-bought stocks (negative quantities). To compensate for it,
        # let's compute how many stock we can actually buy.
        if to_buy > 0:
            total_to_buy += stock_price * to_buy

    ideal_buy = utils.sort_dict(ideal_buy)
    possible_buy = {name: quantity * money /
                    total_to_buy for name, quantity in ideal_buy.items()}
    print(f'total_to_buy={total_to_buy : .2f}')
    print('Ideal buy:')
    utils.print_dict(ideal_buy)

    utils.print_red('Possible buy:')
    utils.print_dict(possible_buy)

    # TODO(safa): Use ceiled values using dividends.


if __name__ == '__main__':
    # Let say I have 20K USD "additional" money to invest.
    stock_to_buy(20000)
