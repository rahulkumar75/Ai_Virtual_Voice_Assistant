import requests
from bs4 import BeautifulSoup

def get_cricket_scores():
    # url = "https://www.espncricinfo.com/"
    url = "https://www.cricbuzz.com/cricket-match/live-scores/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        live_matches = soup.find_all('div', class_='scorecard-container')

        if not live_matches:
            print("No live matches currently.")
            return

        for match in live_matches:
            match_title = match.find('h2').text.strip()
            match_status = match.find('div', class_='status').text.strip()
            score = match.find('span', class_='score').text.strip()
            print(f"Match: {match_title}")
            print(f"Status: {match_status}")
            print(f"Score: {score}")
            print()

    else:
        print("Failed to fetch cricket scores.")

get_cricket_scores()
