import tkinter as tk
from tkinter import messagebox, Menu, Toplevel, Label, Entry, Button, END, Listbox, Scrollbar
import sqlite3

# ----------------- Database Operations -----------------
def init_db():
    """Initialize the database and create table if it does not exist."""
    conn = sqlite3.connect('coins.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS coins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def fetch_coins():
    #Retrieve all coin records from the database.
    conn = sqlite3.connect('coins.db')
    c = conn.cursor()
    c.execute("SELECT * FROM coins")
    rows = c.fetchall()
    conn.close()
    return rows

def add_coin_to_db(name, value):
    #Add a new coin record to the database.
    conn = sqlite3.connect('coins.db')
    c = conn.cursor()
    c.execute("INSERT INTO coins (name, value) VALUES (?, ?)", (name, value))
    conn.commit()
    conn.close()

def update_coin_in_db(coin_id, name, value):
    #Update an existing coin record.
    conn = sqlite3.connect('coins.db')
    c = conn.cursor()
    c.execute("UPDATE coins SET name=?, value=? WHERE id=?", (name, value, coin_id))
    conn.commit()
    conn.close()

def delete_coin_from_db(coin_id):
    #Delete a coin record from the database.
    conn = sqlite3.connect('coins.db')
    c = conn.cursor()
    c.execute("DELETE FROM coins WHERE id=?", (coin_id,))
    conn.commit()
    conn.close()

# ----------------- Tkinter Application -----------------
class CoinApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Coin Manager")
        self.geometry("550x400")
        self.create_menu()
        self.create_widgets()
        self.refresh_list()

    def create_menu(self):
        """Creates a navigation menu."""
        menubar = Menu(self)
        
        # File Menu with Exit option
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Help Menu with About option
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Coin Manager v1.0\nTkinter GUI with SQLite3"))
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.config(menu=menubar)

    def create_widgets(self):
        """Set up the UI components."""
        # Listbox to display coin records
        self.coin_list = Listbox(self, height=15, width=60)
        self.coin_list.pack(pady=20, padx=20)
        
        # Scrollbar for the listbox
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.coin_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.coin_list.yview)
        
        # Button frame for CRUD operations
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        
        Button(btn_frame, text="Add Coin", width=15, command=self.open_add_coin_window).grid(row=0, column=0, padx=5)
        Button(btn_frame, text="Update Coin", width=15, command=self.open_update_coin_window).grid(row=0, column=1, padx=5)
        Button(btn_frame, text="Delete Coin", width=15, command=self.delete_coin).grid(row=0, column=2, padx=5)

    def refresh_list(self):
        """Refresh the listbox with coins from the database."""
        self.coin_list.delete(0, END)
        for coin in fetch_coins():
            # Display format: ID | Name - $Value
            display_text = f"ID: {coin[0]} | {coin[1]} - ${coin[2]:.2f}"
            self.coin_list.insert(END, display_text)

    def open_add_coin_window(self):
        """Open a new window to add a coin."""
        add_window = Toplevel(self)
        add_window.title("Add Coin")
        add_window.geometry("300x200")
        add_window.grab_set()  # Modal window
        
        Label(add_window, text="Coin Name:").pack(pady=5)
        name_entry = Entry(add_window)
        name_entry.pack(pady=5)
        
        Label(add_window, text="Coin Value:").pack(pady=5)
        value_entry = Entry(add_window)
        value_entry.pack(pady=5)
        
        def add_coin_action():
            name = name_entry.get().strip()
            try:
                value = float(value_entry.get())
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid number for value.")
                return
            if not name:
                messagebox.showerror("Input Error", "Coin name cannot be empty.")
                return
            add_coin_to_db(name, value)
            messagebox.showinfo("Success", "Coin added successfully!")
            self.refresh_list()
            add_window.destroy()
        
        Button(add_window, text="Add", command=add_coin_action).pack(pady=10)

    def open_update_coin_window(self):
        """Open a window to update the selected coin."""
        try:
            selected_index = self.coin_list.curselection()[0]
            selected_text = self.coin_list.get(selected_index)
            # Extract coin ID from displayed text
            coin_id = int(selected_text.split("|")[0].split(":")[1].strip())
        except IndexError:
            messagebox.showerror("Selection Error", "Please select a coin to update.")
            return

        # Retrieve current record details from the database
        conn = sqlite3.connect('coins.db')
        c = conn.cursor()
        c.execute("SELECT * FROM coins WHERE id=?", (coin_id,))
        coin = c.fetchone()
        conn.close()

        if not coin:
            messagebox.showerror("Error", "Coin record not found!")
            return

        update_window = Toplevel(self)
        update_window.title("Update Coin")
        update_window.geometry("300x200")
        update_window.grab_set()  # Modal window
        
        Label(update_window, text="Coin Name:").pack(pady=5)
        name_entry = Entry(update_window)
        name_entry.insert(0, coin[1])
        name_entry.pack(pady=5)
        
        Label(update_window, text="Coin Value:").pack(pady=5)
        value_entry = Entry(update_window)
        value_entry.insert(0, str(coin[2]))
        value_entry.pack(pady=5)
        
        def update_coin_action():
            new_name = name_entry.get().strip()
            try:
                new_value = float(value_entry.get())
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid number for value.")
                return
            if not new_name:
                messagebox.showerror("Input Error", "Coin name cannot be empty.")
                return
            update_coin_in_db(coin_id, new_name, new_value)
            messagebox.showinfo("Success", "Coin updated successfully!")
            self.refresh_list()
            update_window.destroy()
        
        Button(update_window, text="Update", command=update_coin_action).pack(pady=10)

    def delete_coin(self):
        #Delete the selected coin record after confirmation.
        try:
            selected_index = self.coin_list.curselection()[0]
            selected_text = self.coin_list.get(selected_index)
            coin_id = int(selected_text.split("|")[0].split(":")[1].strip())
        except IndexError:
            messagebox.showerror("Selection Error", "Please select a coin to delete.")
            return
        
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected coin?"):
            delete_coin_from_db(coin_id)
            messagebox.showinfo("Deleted", "Coin deleted successfully!")
            self.refresh_list()

if __name__ == "__main__":
    init_db()  # Initialize the database on application start
    app = CoinApp()
    app.mainloop()

