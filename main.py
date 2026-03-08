import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("API_KEY")


def get_top_games():
    url = 'https://api.rawg.io/api/games'
    params = {
        "key": api_key,
        "genres": "strategy",
        "tags": "multiplayer",
        "page_size": 10,
        "metacritic": "1,100"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    games = response.json()
    return games


def get_screenshots(slug):
    url = f"https://api.rawg.io/api/games/{slug}/screenshots"
    params={
        "key": api_key
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    screenshots = response.json()
    return [screenshot["image"] for screenshot in screenshots["results"]]


def get_stores(game_id):
    url = f"https://api.rawg.io/api/games/{game_id}/stores"
    params = {
        "key": api_key
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()

def main():

    games = get_top_games()

    for game in games["results"]:
        name = game["name"]
        released = game["released"]
        slug = game["slug"]
        game_id = game["id"]

        print(f"\nНазвание игры: {name}")
        print(f"Дата выхода: {released}")
        print(f"Ссылка на игру: https://api.rawg.io/api/games/{slug}")
        print("Скриншоты игры: ")
        screenshots = get_screenshots(slug)
        for screenshot in screenshots:
            print(screenshot)

        stores = get_stores(game_id)
        print("Где купить:")
        for store in stores["results"]:
            store_url = store['url']
            print(store_url)
    

if __name__ == "__main__":
    main()


