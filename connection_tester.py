import requests
import random
import headers

validated_cookie = headers.cookies
random_header = random.choice(headers.headers_list)

r = requests.session()
r.headers = random_header

response = requests.get('https://www.funda.nl/koop/maastricht/0-300000/sorteer-datum-af/', cookies=validated_cookie).text

if "We houden ons platform graag veilig en spamvrij." in response:
        print("The cookie is no longer valid!")
else:
        print("The cookie is still valid!")
