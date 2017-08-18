from bs4 import BeautifulSoup

soup = BeautifulSoup(open('.dotabuff-content/heroes/content', 'r'), 'html.parser')

heroes = [hero.get('href').split('/')[-1] for hero in soup.find('div', class_='hero-grid').find_all('a')]

print '\n'.join(heroes)
