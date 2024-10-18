import requests
from bs4 import BeautifulSoup

base = 'https://transcripts.foreverdreaming.org/'
response = requests.get(f'{base}viewforum.php?f=205')
soup = BeautifulSoup(response.content, 'html.parser')

li_tags = soup.find_all('li', class_='row')
for li in li_tags[1:]:
    ep = li.find('a',class_='topictitle')
    title = ep.text
    if int(title[1]) == 0:
        continue
    file_name = f'S{title[1]}ep{title[3:5]}'
    link = ep['href'][1:]
    ep_scrape = requests.get(f'{base}{link}')
    ep_soup = BeautifulSoup(ep_scrape.content,'html.parser')
    content = ep_soup.find('div',class_='content')
    with open(f'./ep-trans/{file_name}.txt','w') as file:
        file.write(title+'\n')
        file.write(str(content))
