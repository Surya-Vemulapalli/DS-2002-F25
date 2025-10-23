#!/usr/bin/env python3
import pandas as pd
import os
import sys



def generate_summary(portfolio_file):
    if not os.path.exists(portfolio_file):
        print("File not found",file=sys.stderr)
        sys.exit(1)
    df = pd.read_csv(portfolio_file)
    if df.empty:
        print("Dataframe is empty")
        return
    total_portfolio_value = df['card_market_value'].sum()
    most_valuable_card_index = df['card_market_value'].idxmax()
    most_valuable_card = df.loc[[most_valuable_card_index]]
    
    print(f"The total portfolio costs {total_portfolio_value:.2f} dollars and the most valuable card's details: {most_valuable_card.values}")

def main():
    generate_summary('card_portfolio.csv')

def test():
    generate_summary('test_card_portfolio.csv')

if __name__ == "__main__":
    test()