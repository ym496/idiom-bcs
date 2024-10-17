import requests
from bs4 import BeautifulSoup

base = 'https://transcripts.foreverdreaming.org/'
response = requests.get(f"{base}viewforum.php?f=205")
soup = BeautifulSoup(response.content, 'html.parser')

li_tags = soup.find_all('li', class_='row')
for li in li_tags[1:]:
    ep = li.find('a',class_='topictitle')
    title = ep.text
    link = ep['href']
