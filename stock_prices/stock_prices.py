#!/usr/bin/python

import argparse


def find_max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    if sorted(prices, reverse=True) == prices:
        max_profit = prices[1] - prices[0]
        for index in range(2, len(prices) - 1):
            if prices[index + 1] - prices[index] > max_profit:
                max_profit = prices[index + 1] - prices[index]
    else:
        for index in range(1, len(prices)):
            if prices[index] <= min_price:
                min_price = prices[index]
            else:
                if prices[index] - min_price > max_profit:
                    max_profit = prices[index] - \
                        min_price

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
