import requests
from bs4 import BeautifulSoup
import os

ESPN_URL = 'https://www.espncricinfo.com/live-cricket-score'

def fetch_live_score():
    try:
        response = requests.get(ESPN_URL)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        team1_name = soup.find_all(class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')[0].text.strip()
        team2_name = soup.find_all(class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')[1].text.strip()
        match_date = soup.find(class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3').text.strip()
        match_status = soup.find(class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo').text.strip()

        live_score_info = f"**Match:** {team1_name} vs {team2_name}\n" \
                          f"**Details:** {match_date}\n" \
                          f"**Status:** {match_status}"

        return live_score_info
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    live_score = fetch_live_score()
    if live_score.startswith("**Match:"):
        print(live_score)
    else:
        print("No live scores available! Try again later.")

