import tkinter as tk
from tkinter import messagebox

class PortfolioTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Portfolio Tracker")
        self.root.geometry("500x400")
        
        # Create the main header label
        self.header_label = tk.Label(root, text="Portfolio Tracker", font=("Helvetica", 16, "bold"))
        self.header_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Entry widgets for Stock Symbol and Stock Price
        self.stock_symbol_label = tk.Label(root, text="Stock Symbol:")
        self.stock_symbol_label.grid(row=1, column=0, padx=10, pady=5)
        self.stock_symbol_entry = tk.Entry(root)
        self.stock_symbol_entry.grid(row=1, column=1, padx=10, pady=5)

        self.stock_price_label = tk.Label(root, text="Stock Price:")
        self.stock_price_label.grid(row=2, column=0, padx=10, pady=5)
        self.stock_price_entry = tk.Entry(root)
        self.stock_price_entry.grid(row=2, column=1, padx=10, pady=5)

        # Add stock button
        self.add_button = tk.Button(root, text="Add Stock", command=self.add_stock)
        self.add_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Listbox to show stocks in the portfolio
        self.portfolio_listbox = tk.Listbox(root, width=50, height=10)
        self.portfolio_listbox.grid(row=4, column=0, columnspan=3, pady=10)

        # Buttons for removing and updating stock prices
        self.remove_button = tk.Button(root, text="Remove Stock", command=self.remove_stock)
        self.remove_button.grid(row=5, column=0, pady=5)

        self.update_button = tk.Button(root, text="Update Stock Price", command=self.update_stock)
        self.update_button.grid(row=5, column=1, pady=5)

        # List to hold portfolio data (list of dictionaries)
        self.portfolio = []

    def add_stock(self):
        symbol = self.stock_symbol_entry.get().upper()
        price = self.stock_price_entry.get()

        if symbol and price:
            try:
                price = float(price)
                self.portfolio.append({"symbol": symbol, "price": price})
                self.update_portfolio_display()
                self.clear_inputs()
            except ValueError:
                messagebox.showerror("Invalid Price", "Please enter a valid price.")
        else:
            messagebox.showerror("Missing Information", "Both fields must be filled.")

    def remove_stock(self):
        selected_index = self.portfolio_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.portfolio.pop(index)
            self.update_portfolio_display()
        else:
            messagebox.showwarning("No Selection", "Please select a stock to remove.")

    def update_stock(self):
        selected_index = self.portfolio_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_price = self.stock_price_entry.get()

            if new_price:
                try:
                    new_price = float(new_price)
                    self.portfolio[index]["price"] = new_price
                    self.update_portfolio_display()
                    self.clear_inputs()
                except ValueError:
                    messagebox.showerror("Invalid Price", "Please enter a valid price.")
            else:
                messagebox.showerror("No Price", "Please enter the new price to update.")
        else:
            messagebox.showwarning("No Selection", "Please select a stock to update.")

    def update_portfolio_display(self):
        self.portfolio_listbox.delete(0, tk.END)
        for stock in self.portfolio:
            self.portfolio_listbox.insert(tk.END, f"{stock['symbol']} - ${stock['price']:.2f}")

    def clear_inputs(self):
        self.stock_symbol_entry.delete(0, tk.END)
        self.stock_price_entry.delete(0, tk.END)


# Create the main window and pass it to the PortfolioTracker
if __name__ == "__main__":
    root = tk.Tk()
    app = PortfolioTracker(root)
    root.mainloop()

