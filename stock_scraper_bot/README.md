##
- Author
- Ashirbad Roul
- Email: ashirbad.r@phytecembedded.in

# Stock Scraper Bot


A Python automation script that scrapes stock data from Google, saves the results to a CSV file, and sends the file via email. You can schedule it to run daily at a specific time using a cron job.

## Features

- Scrapes current stock price for specified symbols (e.g., AAPL)
- Saves extracted data into a CSV file named with the current date
- Sends an email with the CSV file as an attachment
- Can be automated to run daily

## Project Structure

stock_scraper_bot/ 
	|
	├── scraper.py # Main script 
	├── requirements.txt # Python dependencies 
	├── venv/ # Python virtual environment 
	└── README.md # Project documentation

#Create and activate a Python virtual environment

$python3 -m venv venv
$source venv/bin/activate

#Install required Python packages

$pip install -r requirements.txt

##Edit scraper.py and update the following variables with your email credentials and target email address:

- email_sender = "your_email@gmail.com"
- email_receiver = "receiver_email@example.com"
- password = "your_app_password"  # 16-character App Password from Google

#To schedule the script to run daily at 9:00 AM:

$crontab -e

#Add the .py path line (adjust the path accordingly):


