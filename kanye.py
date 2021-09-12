import requests

# need to get input of username
SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/am12012195/playlists'
ACCESS_TOKEN = 'BQB0i-o5nKZ_fHhIXUFmCxzC3CXv4eshK1MAdvFUnjrmKtKyOGWTOWWEj5oFbL01cx84xg020d2eqNwF7xoZMLD-Byc2lMOIQYQMnSkhm9COdl54X5kEJjeRm87Jx6OoT7BPBZUS29sZlBVC3Umsyr6Zy1HRSr18ftQiuSIHpXJnJBto_GNNMz8dlY6ptanHRS6_u5Ja'

def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp

def main():
    playlist = create_playlist_on_spotify(
        name="indie type beat",
        public=False
    )

    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()