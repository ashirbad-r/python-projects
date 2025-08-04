# Tkinter Coin Manager

A desktop application built with Python’s Tkinter for the GUI and SQLite3 for database operations. This project allows you to manage coin records by performing the following operations:
- **Connect to a Database:** Create and connect to an SQLite3 database.
- **Display Records:** Fetch data from the database and display it in a Listbox.
- **CRUD Operations:**  
  - **Add Coin:** Open a new dialog to insert a new coin record.  
  - **Update Coin:** Modify an existing record.  
  - **Delete Coin:** Remove a record from the database.
- **Multiple Layers:** Manage multiple dialogs using Toplevel windows.
- **Notification System:** Use popup message boxes to provide user feedback.
- **Navigation Menu:** Implement a menu bar (File and Help menus) for easy navigation.

## Features

- SQLite3-based persistent storage for coin records.
- A user-friendly Tkinter GUI with separate dialogs for each operation.
- Notification popups for successful and error actions.
- A navigation menu for basic file and help options.

## Requirements

- Python 3.x
- Tkinter (install via `sudo apt-get install python3-tk` on Debian/Ubuntu)
- Make sure SQLite3 is included in your system

## How to Run

---

   $vi app.py
   $python3 app.py
   $sudo apt install sqlite3
   $pip install db-sqlite3 
   $sudo snap install sqlitebrowser
   $sqlitebrowser &

---


## Usage

- **Add Coin:** Click the "Add Coin" button, enter the coin's name and value in the popup, and click Add.
- **Update Coin:** Select a coin from the list and click "Update Coin." Modify the fields in the popup and click Update.
- **Delete Coin:** Select a coin from the list and click "Delete Coin," then confirm the deletion.
- **Menu Options:** Use the menu bar for additional actions like exiting the app or viewing the About information.

## Project Structure

├── app.py # Main source code for the application 
├── coins.db # SQLite3 database file (created automatically) 
└── README.md # Project documentation

