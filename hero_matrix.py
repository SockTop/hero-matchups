import pkg_resources
import subprocess

import click

from analysis.matchup_analyzer import MatchupAnalyzer


def pretty_print_rankings(rankings, output_count=20, reverse=True):
    print 'Heroes:\t\t\tAdvantages'
    print '--------------------------------------------------'
    for hero, advantage in sorted(rankings, key=lambda x: x[1], reverse=reverse)[:output_count]:
        print '{hero}{fill}{advantage}'.format(hero=hero, advantage=str(advantage), fill=' ' * (30 - len(hero) - len(str(advantage))))


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.pass_context
@click.argument('opposing_heroes')
@click.option('--heroes', help="A list of heroes to rank")
@click.option('--players', help="A list of players whose heroes should be ranked")
def rank_options(ctx, opposing_heroes, heroes=None, players=None):
    opposing_heroes = opposing_heroes.split(',')

    if heroes is None:
        if players is None:
            rankings = ctx.obj.rank_options_for_team(opposing_heroes)
        else:
            rankings = ctx.obj.rank_options_for_team(opposing_heroes, players.split(','))
    else:
        rankings = ctx.obj.rank_options(heroes.split(','), opposing_heroes)

    print 'Top 20 favorable picks:'
    pretty_print_rankings(rankings)

@cli.command()
@click.pass_context
@click.argument('heroes')
def suggest_bans(ctx, heroes):
    totals = ctx.obj.calculate_combined_matchups(heroes.split(','))
    
    print 'Top 20 least favorable matchups with current picks:'
    pretty_print_rankings(totals.items(), reverse=False)


def main():
    try:
        open('.matchups.json', 'r')
    except IOError:
        print 'Initializing hero matchup data'

        subprocess.call(['/bin/bash', pkg_resources.resource_filename('retrieval', 'initialize.sh')])

    analyzer = MatchupAnalyzer()

    cli(obj=analyzer)


if __name__ == '__main__':
    main()
