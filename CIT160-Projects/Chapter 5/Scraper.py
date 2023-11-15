# Made by Connor Hackenberg
# Date Started: 10/23/23
# Program Importance: Will use the beautiful soup module the PCT website.
# Contact: https://connorhackenberg.tech/
# Mirrored on GitHub github.com/MapGuy11
from bs4 import BeautifulSoup
import requests

url = "https://www.pct.edu"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html")

links = soup.find_all('a')