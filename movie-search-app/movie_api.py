import requests
from config import API_KEY

BASE_URL = "http://www.omdbapi.com/"

def get_movie(movie_name):
    params = {
        "apikey" : API_KEY,
        "t" : movie_name
    }
    try: 
        response = requests.get(BASE_URL, params = params, timeout = 5)

        if response.status_code != 200:
            return None

        data = response.json()

        if data["Response"] == "False":
            return None

        return data

    except requests.exceptions.ConnectionError:
        return None
    except requests.exceptions.Timeout:
        return None
    except requests.exceptions.RequestException:
        return None