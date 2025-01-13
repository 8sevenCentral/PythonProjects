import requests
import urllib
from datetime import datetime

BASE_URL = 'https://api.prop-odds.com'
API_KEY = 'IptO50IbNKXm8TOHwUPQ5tjblG5ASItDXsC9gMAwgc'


def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

    print('Request failed with status:', response.status_code)
    return {response.status_code}


def get_nhl_games():
    now = datetime.now()
    query_params = {
        'date': now.strftime('%Y-%m-%d'),
        'tz': 'America/New_York',
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/games/nhl?' + params
    return get_request(url)

now = datetime.now()
query_params = {
        'date': now.strftime('%Y-%m-%d'),
        'tz': 'America/New_York',
        'api_key': API_KEY,
    }
params = urllib.parse.urlencode(query_params)
url = BASE_URL + '/beta/games/nhl?' + params
response = requests.get(url)

if response.status_code == 200:
    
    game_data = response.json()
    game_id = game_data[0]['GameID']
    print(f'The most recent game ID is: {game_id}')
else:
    print(f'Request failed with status code: {response.status_code}')

def get_odds_data(url, api_key):
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/games/nhl?' + params
    response = requests.get(url)
    return response.json()

def parse_odds_data(odds_data):
    parsed_odds_data = {}
    for odds in odds_data:
        parsed_odds_data[odds['MatchId']] = {
            'home_team': odds['HomeTeam'],
            'away_team': odds['AwayTeam'],
            'home_odds': odds['HomeOdds'],
            'draw_odds': odds['DrawOdds'],
            'away_odds': odds['AwayOdds'],
        }
    return parsed_odds_data

def process_odds_data(url, api_key):
    odds_data = get_odds_data(url, api_key)
    parsed_odds_data = parse_odds_data(odds_data)
    return parsed_odds_data