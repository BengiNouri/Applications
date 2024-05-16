import requests
from config.settings import config

class PokeAPI:
    def __init__(self):
        self.base_url = config.POKEAPI_BASE_URL

    def get_data(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

# Example usage
if __name__ == "__main__":
    poke_api = PokeAPI()
    data = poke_api.get_data("pokemon?limit=10")  # Get the first 10 Pokémon
    print(data)
