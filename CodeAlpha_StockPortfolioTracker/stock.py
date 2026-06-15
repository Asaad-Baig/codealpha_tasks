import os

def stock_portfolio_tracker():
    print("Welcome to the Stock Portfolio Tracker!")
    print("---------------------------------------")
    
    stock_market_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGL": 175.00,
        "AMZN": 185.00,
        "MSFT": 420.00
    }
    
    user_portfolio = {}
    
    # Display available stocks in the market
    print("Available stocks in our market database:")
    for ticker, price in stock_market_prices.items():
        print(f"  - {ticker}: ${price:.2f}")
    print("---------------------------------------")

    while True:
        ticker = input("\nEnter stock ticker symbol to add (or type 'done' to calculate): ").upper().strip()
        
        if ticker == 'DONE':
            break
            
        if ticker not in stock_market_prices:
            print(f"❌ '{ticker}' is not available in our market database. Please try another one.")
            continue
            
        try:
            quantity = int(input(f"Enter number of shares for {ticker}: "))
            if quantity <= 0:
                print("❌ Quantity must be a positive number.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a whole number for shares.")
            continue
            
        # Add or update the stock in the user's portfolio
        if ticker in user_portfolio:
            user_portfolio[ticker] += quantity
        else:
            user_portfolio[ticker] = quantity
            
        print(f"✅ Added {quantity} shares of {ticker} to your tracking list.")

    if not user_portfolio:
        print("\nYour portfolio is empty. Exiting tracker.")
        return

    print("\n=======================================")
    print("       YOUR INVESTMENT SUMMARY         ")
    print("=======================================")
    
    total_portfolio_value = 0.0
    summary_lines = [] # Collected to write to a file later
    
    # Header format
    header = f"{'Stock':<10}{'Shares':<10}{'Price':<12}{'Total Value':<12}"
    print(header)
    print("-" * 45)
    summary_lines.append(header + "\n" + ("-" * 45) + "\n")
    
    for ticker, shares in user_portfolio.items():
        price = stock_market_prices[ticker]
        item_total = shares * price
        total_portfolio_value += item_total
        
        line = f"{ticker:<10}{shares:<10}${price:<11.2f}${item_total:<11.2f}"
        print(line)
        summary_lines.append(line + "\n")
        
    print("-" * 45)
    footer = f"{'TOTAL PORTFOLIO INVESTMENT VALUE:':<32}${total_portfolio_value:,.2f}"
    print(footer)
    print("=======================================")
    summary_lines.append(("-" * 45) + "\n" + footer + "\n")

    save_choice = input("\nWould you like to save this summary to a text file? (yes/no): ").lower().strip()
    if save_choice in ['yes', 'y']:
        filename = "portfolio_summary.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write("STOCK PORTFOLIO TRACKER REPORT\n")
            file.write("=======================================\n")
            file.writelines(summary_lines)
            
        print(f"💾 Success! Summary saved locally to '{os.path.abspath(filename)}'")
    else:
        print("Summary not saved.")

if __name__ == "__main__":
    stock_portfolio_tracker()