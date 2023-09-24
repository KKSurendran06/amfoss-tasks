import requests
from bs4 import BeautifulSoup
import os

ESPN_URL = 'https://www.espncricinfo.com/live-cricket-score'

def fetch_live_score():
    try:
        response = requests.get(ESPN_URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        team1_name = soup.find_all(class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')[0].text.strip()
        team2_name = soup.find_all(class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')[1].text.strip()
        match_info = soup.find(class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3').text.strip()
        match_status = soup.find(class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo').text.strip()
        
        live_score_info = f"**Team1:** {team1_name}\n" \
                          f"**Team2:** {team2_name}\n"  \
                          f"**Details:** {match_info}\n" \
                          f"**Status:** {match_status}\n" \

        return live_score_info
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    live_score = fetch_live_score()
    if live_score.startswith("**Match:"):
        print(live_score)
    else:
        print("No live scores available! Try again later.")

