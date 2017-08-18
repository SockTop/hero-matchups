from collections import defaultdict
import glob
import json


class MatchupAnalyzer(object):
    def __init__(self):
        with open('.matchups.json', 'r') as f:
            self.matchups = json.loads(f.read())

    def calculate_combined_matchups(self, heroes):
        totals = defaultdict(lambda: 0)        

        for hero in heroes:
            for enemy, advantage in self.matchups[hero].items():
                totals[enemy] += advantage
        return totals

    def rank_options(self, hero_options, opposing_heroes):
        totals = defaultdict(lambda: 0)
        for hero in hero_options:
            for enemy in opposing_heroes:
                if hero == enemy:
                    try:
                        del totals[hero]
                    except KeyError:
                        pass
                    break
                
                totals[hero] += self.matchups[hero][enemy]
    
        return sorted([(hero, totals[hero]) for hero in set(hero_options)], key=lambda x: x[1], reverse=True)

    def rank_options_for_team(self, opposing_heroes, players=None):
        data_files = []
        if players is None:
            data_files = glob.glob('data/heroes/*.json')
        else:
            for player in players:
                data_files.append('data/heroes/{}.json'.format(player))
        
        heroes = []
        for file in data_files:
            heroes.extend(json.load(open(file, 'r')))
        
        return self.rank_options(heroes, opposing_heroes)
