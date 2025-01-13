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
    return {}


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


def get_game_info(game_id):
    query_params = {
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/game/' + game_id + '?' + params
    return get_request(url)


def get_markets(game_id):
    query_params = {
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/markets/' + game_id + '?' + params
    return get_request(url)


def get_most_recent_odds(game_id, market):
    query_params = {
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/odds/' + game_id + '/' + market + '?' + params
    return get_request(url)


def main():
    games = get_nhl_games()
    first_game = games['games'][0]
    game_id = first_game['game_id']
    print(first_game)
    game_info = get_game_info(game_id)
    print(game_info)

    if len(games['games']) == 0:
        print('No games scheduled for today.')
        return
    
    markets = get_markets(game_id)
    print(markets)
    #if len(markets['markets']) == 0:
    #     print('No markets found.')
    #     return

    market = markets['markets'][0]
    print(market)
    odds = get_most_recent_odds(game_id, market['name'])
    print(odds)



if __name__ == '__main__':
    main()
