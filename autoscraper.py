
# scrape our own website

import requests

r = requests.get('http://localhost:5000/movielist')
print(r.json())


# trying a dDos attack on ourself - does not crash anything
for i in range(1000):
    requests.get('http://localhost:5000/movielist')

# scraping the HTML page
r = requests.get('http://localhost:5000/recommender?movie=Titanic&rating=5')
print(r.text)
