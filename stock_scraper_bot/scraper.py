#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# --- Configuration ---
URL = "https://finance.yahoo.com/quote/AAPL/"
HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "ashirbad.roul2019@gift.edu.in"
SENDER_PASSWORD = "bqlg pajx vjgl neva"  # WARNING: Use app-specific password if 2FA is enabled!
RECIPIENTS = ["bantyroulroul@gmail.com"]

# --- Email Functions ---
def send_email_with_attachment(sender, recipients, subject, body, attachment_path, smtp_server, smtp_port, username, password):
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {attachment_path}")
    msg.attach(part)
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(sender, recipients, msg.as_string())
        print("Email sent successfully!")

# --- Scraping Functions ---
def scrape_page(url, headers):
    time.sleep(2)
    response = requests.get(url, headers=headers, timeout=60)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup

def extract_stock_data(soup):
    print("Extracting stock data...")
    data = []

    try:
        symbol = URL.split("/")[-2]

        # Current stock price
        price_span = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})
        price = price_span.get_text(strip=True) if price_span else "N/A"

        # Volume
        volume_td = soup.find("td", {"data-test": "TD_VOLUME-value"})
        volume = volume_td.get_text(strip=True) if volume_td else "N/A"

        data.append([symbol, price, volume])
        print(f"Extracted data: {data}")
    except Exception as e:
        print(f"Error extracting stock data: {e}")

    return data

def save_to_csv(data):
    today_str = datetime.now().strftime("%Y%m%d")
    filename = "stock_data_{today_str}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Symbol", "Price", "Volume"])
        for row in data:
            writer.writerow(row)
    print(f"Data saved to {filename}")
    return filename

# --- Main Process ---
def main():
    soup = scrape_page(URL, HEADERS)
    stock_data = extract_stock_data(soup)

    if stock_data:
        csv_filename = save_to_csv(stock_data)
        subject = "Daily Stock Report - " + datetime.now().strftime("%Y-%m-%d")
        body = "Hello Ashirbad,\n\nPlease find attached today's stock report.\n\nRegards,\nYour Scraping Bot"
        send_email_with_attachment(
            SENDER_EMAIL, RECIPIENTS, subject, body,
            csv_filename, SMTP_SERVER, SMTP_PORT,
            SENDER_EMAIL, SENDER_PASSWORD
        )
    else:
        print("No stock data found. Email not sent.")

if __name__ == "__main__":
    main()

