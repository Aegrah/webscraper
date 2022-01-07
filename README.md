# webscraper
This web scraper is created as a hobby project to learn a bit of Python. 

The scraper is currently configured to scrape the Dutch Funda property advertisement website for new properties. Once it finds a property, an e-mail notification is sent out to the user with any interesting information regarding the property.

Can be hosted on a VPS or hosting platform such as pythonanywhere or Heroku in order to run infinitely. 

To do's:
- Telegram bot to push notifications
- Evade robot checks:
  - ~~Set randomized sleep timers
  - ~~Set randomized user-agents
  - ~~Set scraping times at working hours (8 PM - 7 PM)
- Add user options:
  - Allow users to specify URL
  - Set user properties (type of house, price, neighbourhood etc.)
