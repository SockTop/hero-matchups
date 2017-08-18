# hero-matchups
A simple tool to help with common drafting questions. 

This tool scrapes publicly listed hero matchup data from Dotabuff, parses it into a matrix of hero advantages/disadvantages, and provides a CLI wrapper for a few common commands. As these matchups are aggregate values taken across all games played at all skill levels, they should not be considered 100% accurate, and are more intended to suggest options during drafting.

## Installation
This package can be installed via
```
pip install -r requirements.txt && python setup.py install
```
This will make an executable named `matchups` available on your path, however (because I'm lazy) it must be run from the root level directory of this project.

## Commands
This tool supports two commands:
  - `rank_options` - rank a list of heroes against a list of opposing heroes. E.g. "given that they have picked Sven and Dazzle, which of my heroes have the largest advantage against them".
  - `suggest_bans` - propose a list of heroes to ban based against a list of "your" heroes. E.g. "given that we've picked Phantom Assassin and Earth Spirit, who should we ban?"
