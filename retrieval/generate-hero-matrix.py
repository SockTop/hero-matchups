import json
import os

from bs4 import BeautifulSoup

def fetch_hero_matchups(hero):  
    soup = BeautifulSoup(open('/users/samuelsilberstein/workspace/hero-matrix/.dotabuff-content/heroes/{}/matchups'.format(hero), 'r'), 'html.parser')
    
    matchups = soup.find_all('tbody')[1].find_all('tr')
    
    results = {
        'hero': soup.find('h1').contents[0],
        'matchups': {}
    }
    
    for matchup in matchups:
        cells = matchup.find_all('td')
        
        results['matchups'][cells[0].get('data-value')] = float(cells[2].get('data-value'))
        
    return results

def generate_matrix():
    matchups = {}
    for hero in os.listdir('/users/samuelsilberstein/workspace/hero-matrix/.dotabuff-content/heroes'):
        try:
            matchup = fetch_hero_matchups(hero)

            matchups[matchup['hero']] = matchup['matchups']
        except IOError:
            pass
        
    return matchups

if __name__ == '__main__':
    matchups = generate_matrix()

    with open('.matchups.json', 'w') as f:
        f.write(json.dumps(matchups))
