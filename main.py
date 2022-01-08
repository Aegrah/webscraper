# Imports for main
from bs4 import BeautifulSoup
import requests
import sys

# Randomizing request headers and time
import random
from random import randint
import time
from time import sleep
from collections import OrderedDict
from typing import OrderedDict

# Import headers from headers.py
import headers

# To send email
import smtplib

# Dealing with credentials
sys.path.append("/home/aegrah/development/credentials")
import credentials
username = credentials.username
password = credentials.password

# Set time variables
start = time.time()
time_to_exit = 43200 # 12 hours

# Set global variables
funda_url = "https://www.funda.nl"
request_url = "/koop/maastricht/0-300000/sorteer-datum-af/"
validated_cookie = headers.cookies
uids = []

# Set function to send email
def send_email(username, password, message):
    receiver = "r.f.groenewoud98@gmail.com"
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(username, password)
    server.sendmail(username, receiver, message)
    server.quit()

# Set function to create baseline of current UID's
def set_baseline(uids):
    # Get random header
    random_header = random.choice(headers.headers_list)

    # Request the page, and extract the data
    r = requests.session()
    r.headers = random_header
    response = r.get(funda_url + request_url, cookies = validated_cookie).text
    soup = BeautifulSoup(response, "lxml")

    # Extract data from list item on page
    advertisements = soup.find_all("li", {"class":"search-result"})

    # Find uid's for all items in the list
    for advertisement in advertisements:
        try:
            advertisement_href = advertisement.find(href = True)

            # Add unique identifier
            if "appartement" in advertisement_href["href"]:
                uid = advertisement_href["href"][29:37]
            if "huis" in advertisement_href["href"]:
                uid = advertisement_href["href"][22:30]
            
            # Check if there is a new property available
            if uid in uids:
                pass
            # If the unique id is not yet in the list, add the property to a file and save the unique id 
            else:
                uids.append(uid)
        except:
            pass
    return uids

def find_new_advertisements(uids):
    # Get random header
    random_header = random.choice(headers.headers_list)

    # Request the page and extract data
    r = requests.session()
    r.headers = random_header
    response = r.get(funda_url + request_url, cookies = validated_cookie).text
    soup = BeautifulSoup(response, "lxml")

    # Extract data from list item on page
    advertisements = soup.find_all("li", {"class":"search-result"})

    for advertisement in advertisements:
        try:
            r = requests.session()
            r.headers = random_header
            advertisement_href = advertisement.find(href = True)
            funda_advertisement = r.get(funda_url + advertisement_href["href"], cookies = validated_cookie).text
            soup_advertisement = BeautifulSoup(funda_advertisement, "lxml")

            address = soup_advertisement.find("span", {"class":"object-header__title"}).text
            postalcode = soup_advertisement.find("span", {"class":"object-header__subtitle fd-color-dark-3"}).text.replace(" ", "")
            attributes = soup_advertisement.find_all("dd", {"class":"fd-flex--bp-m fd-flex-wrap fd-align-items-center"})
            price_attribute = attributes[0].span.text.strip()
            price = price_attribute[2:9]
            
            split_strings = []
            split_strings.append(postalcode[0:6])
            split_strings.append(postalcode[6:16])
            split_strings.append(postalcode[17:len(postalcode)].strip())

            # Add unique identifier
            if "appartement" in advertisement_href["href"]:
                uid = advertisement_href["href"][29:37]
            if "huis" in advertisement_href["href"]:
                uid = advertisement_href["href"][22:30]
            
            # Check if there is a new property available
            if uid in uids:
                pass
            else:
                # Create message body
                message = f"From: Funda Scraper <web.scraper.funda@gmail.com>\n"
                message += f"To: Ruben Groenewoud <r.f.groenewoud98@gmail.com>\n" 
                message += f"Subject: Nieuwe woning op {address} in {split_strings[2]} beschikbaar!\n"
                message += f"Er is een nieuwe woning beschikbaar op Funda!\n\n"
                message += f"Straat en huisnummer: {address}\n"
                message += f"Postcode: {split_strings[0]}, {split_strings[1]}\n"
                message += f"Wijk: {split_strings[2]}\n"
                message += f"Vraagprijs: {price} euro k.k.\n"
                message += f"Link: {funda_url + advertisement_href['href']}\n"

                # Send the email
                send_email(username, password, message=message)
                
                # Append unique id to the list! 
                uids.append(uid)
        except:
            pass

    return uids

if __name__ == "__main__": 
    # Setting the base line of the current advertisements so we don't get spammed with the first results
    set_baseline(uids)

    # Find new advertisements, if there is none, then sleep and try again in 10 to 20 minutes
    while True:
        find_new_advertisements(uids)
        print("Scraping completed! Sleeping...\n")
        sleep(randint(600, 1200))
        if time.time() > start + time_to_exit: break
