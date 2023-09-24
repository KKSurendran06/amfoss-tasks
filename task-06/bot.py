import discord
import requests
from bs4 import BeautifulSoup
import csv
from dotenv import load_dotenv
import os

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

ESPN_URL = 'https://www.espncricinfo.com/live-cricket-score'

help_message = """
**Cricket Bot Commands:**
- `!livescore`: Generate live cricket score and append it to the CSV file.
- `!csv`: Display match history in CSV format.
- `!help`: Display this help message.
"""

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!livescore'):

        live_score_info = fetch_live_score()
        await message.channel.send(live_score_info)

    elif message.content.startswith('!csv'):

        match_history = fetch_match_history()
        await message.channel.send(file=discord.File('match_history.csv'))

    elif message.content.startswith('!help'):

        await message.channel.send(help_message)

def fetch_live_score():

    response = requests.get(ESPN_URL)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        team1_name = soup.find_all(class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')[0].text.strip()
        team2_name = soup.find_all(class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')[1].text.strip()
        match_date = soup.find(class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3').text.strip()
        match_status = soup.find(class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo').text.strip()

        live_score_info = f"**Match:** {team1_name} vs {team2_name}\n" \
                          f"**Details:** {match_date}\n" \
                          f"**Status:** {match_status}"

        append_to_csv(live_score_info)
        
        return live_score_info

    else:
        return "Failed to fetch live score."

def fetch_match_history():

    try:
        with open('match_history.csv', 'r') as file:
            lines = file.readlines()
        return ''.join(lines)
    except FileNotFoundError:
        return "No match history available."

def append_to_csv(data):

    with open('match_history.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data])

if __name__ == '__main__':
    client.run(bot_token)

