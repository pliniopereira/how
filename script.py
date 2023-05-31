import requests

def get_top_tracks(country, limit):
    api_key = "<API_KEY>"
    url = f"http://ws.audioscrobbler.com/2.0/?method=geo.gettoptracks&country={country}&api_key={api_key}&format=json&limit={limit}"
    
    response = requests.get(url)
    data = response.json()
    
    tracks = data["tracks"]["track"]
    for track in tracks:
        name = track["name"]
        artist = track["artist"]["name"]
        print(f"{name} - {artist}")

if __name__ == "__main__":
    country = "Brazil"  # Código do país (por exemplo, Brazil)
    limit = 10  # Limite de músicas a serem exibidas

    get_top_tracks(country, limit)
