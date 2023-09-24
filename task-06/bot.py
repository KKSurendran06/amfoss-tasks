import discord
from dotenv import load_dotenv
import os
from datetime import datetime
import csv
from scraper import fetch_live_score  

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

help_message = """
**Cricket Bot Commands:**
- `!livescore`: Generate live cricket score and append it to the CSV file.
- `!generate`: Display match history in CSV format.
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

        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        live_score_with_time = f"{timestamp}:\n" + live_score_info
                          
        live_score_with_timestamp = f"{live_score_with_time}"
        append_to_csv(live_score_with_timestamp)

        await message.channel.send(live_score_info)

    elif message.content.startswith('!generate'):
        if "!generate" in message.content.lower():
        
            match_history = fetch_match_history()
            await message.channel.send(file=discord.File('match_history.csv'))

    elif message.content.startswith('!help'):
        await message.channel.send(help_message)

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

