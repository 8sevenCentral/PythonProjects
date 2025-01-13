import requests
import urllib
from datetime import datetime


# Set the API base URL and your API key
BASE_URL = 'https://api.example.com'
API_KEY = 'IptO50IbNKXm8TOHwUPQ5tjblG5ASItDXsC9gMAwgc'

# Define the API endpoints
game_info_endpoint = '/game-info'
game_odds_endpoint = '/game-odds'
draftkings_market = 'DraftKings'  # Replace with the specific market you need

# Set the headers with the API key
headers = {
    'Authorization': f'Bearer {API_KEY}'
}

# Get game info
game_info_response = requests.get(BASE_URL + game_info_endpoint, headers=headers)
if game_info_response.status_code == 200:
    game_info_data = game_info_response.json()
else:
    print(f"Failed to retrieve game info. Status code: {game_info_response.status_code}")

# Get game odds
game_odds_response = requests.get(BASE_URL + game_odds_endpoint, headers=headers)
if game_odds_response.status_code == 200:
    game_odds_data = game_odds_response.json()
else:
    print(f"Failed to retrieve game odds. Status code: {game_odds_response.status_code}")

# Get market data for DraftKings
draftkings_data = [data for data in game_odds_data if data['market'] == draftkings_market]

# Now you can work with game info, game odds, and DraftKings market data
print("Game Info:", game_info_data)
print("Game Odds:", game_odds_data)
print("DraftKings Data:", draftkings_data)
