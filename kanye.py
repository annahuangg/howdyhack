import requests

SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/am12012195/playlists'
ACCESS_TOKEN = 'BQCnCM78HkELInUce2yZ42pyzprfRxFKXNhne7LMv5BZ4a12hMd26jLgutJ56FuKDR7EYhsuee2FFVdasSrB819SPgbmXd0KYqIA6gE0G3AigUfJWmzTFXc9p5RaHOo8wL1-epI7ZwyaUz13nk_ffZOkST2BZ8yti6Rv1hBGDkZKIej6Neu0ZmLrni_NMRaFb_BLH5qO'

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
        name="My Private Playlist",
        public=False
    )

    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()