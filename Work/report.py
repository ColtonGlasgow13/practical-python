# report.py
#
# Exercise 2.4
import csv
from pprint import pprint


def read_portfolio(filename: str) -> list:
    portfolio = []

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)

    return portfolio


def read_prices(filename: str) -> dict:
    prices = {}

    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) > 1:
                prices[row[0]] = float(row[1])

    return prices


def main():
    portfolio = read_portfolio('portfolio.csv')
    prices = read_prices('prices.csv')
    pprint(prices)


if __name__=='__main__':
    main()
