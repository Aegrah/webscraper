from bs4 import BeautifulSoup
import requests
import time

# To send email
import smtplib, ssl
from email.mime.text import MIMEText
import sys

# Dealing with credentials 
sys.path.append("/home/kali/development/credentials")
import credentials
username = credentials.username
password = credentials.password

class Scraper:
    # Set class attributes
    def __init__(self):
        self.funda_url = "https://www.funda.nl"
        self.request_url = "/koop/maastricht/0-300000/sorteer-datum-af/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

    def send_email(self, username, password, message):
        receiver = "r.f.groenewoud98@gmail.com"
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(username, password)
        server.sendmail(username, receiver, message)
        server.quit()
    
    def set_baseline(self, uids):
        # Request the page, and extract the data
        r = requests.get(self.funda_url + self.request_url, headers = self.headers).text
        soup = BeautifulSoup(r, "lxml")
        
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

    def find_new_advertisements(self, uids):
        # Request the page and extract data
        r = requests.get(self.funda_url + self.request_url, headers = self.headers).text
        soup = BeautifulSoup(r, "lxml")
        
        # Extract data from list item on page
        advertisements = soup.find_all("li", {"class":"search-result"})

        for advertisement in advertisements:
            try:
                advertisement_href = advertisement.find(href = True)
                funda_advertisement = requests.get(self.funda_url + advertisement_href["href"], headers = self.headers).text
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
                # If the unique id is not yet in the list, add the property to a file and save the unique id 
                else:
                    # Create message body
                    message = f"From: Ruben Groenewoud <web.scraper.funda@gmail.com>\n"
                    message += f"To: Ruben Groenewoud <r.f.groenewoud98@gmail.com>\n" 
                    message += f"Subject: Nieuwe woning op {address} in {split_strings[2]} beschikbaar!\n"
                    message += f"Er is een nieuwe woning beschikbaar op Funda!\n\n"
                    message += f"Straat en huisnummer: {address}\n"
                    message += f"Postcode: {split_strings[0]}, {split_strings[1]}\n"
                    message += f"Wijk: {split_strings[2]}\n"
                    message += f"Vraagprijs: {price} euro k.k.\n"
                    message += f"Link: {self.funda_url + advertisement_href['href']}\n"
                    
                    # Send the email
                    scraper.send_email(username, password, message=message)

                    # Append unique id to the list! 
                    uids.append(uid)
            except:
                pass
        
        return uids

if __name__ == "__main__":
    scraper = Scraper()
    
    # Define empty list so we can check for unique property ids
    uids = []
    message = ""

    # Setting the base line of the current advertisements so we don't get spammed with the first 10 results
    scraper.set_baseline(uids)

    # Find new advertisements, if there is none, then sleep and try again in 10 minutes
    while True:
        scraper.find_new_advertisements(uids)
        print("Scraping completed! Sleeping for 600 seconds...\n")
        time.sleep(600)