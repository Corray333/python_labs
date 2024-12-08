from domain import add_artist, add_album, add_song, get_all_artists, get_albums_by_artist, get_songs_by_album, get_artist_with_albums_and_songs
from datetime import datetime

def main():
    # Преобразуем строки в даты
    artist_birth_date = datetime.strptime("1990-01-01", "%Y-%m-%d").date()
    album_release_date = datetime.strptime("2010-05-20", "%Y-%m-%d").date()
    
    # Добавление данных
    print("Добавление артиста...")
    artist = add_artist(name="John Doe", genre="Rock", birth_date=artist_birth_date)
    print("Добавлен артист:", artist)

    print("\nДобавление альбома...")
    album = add_album(title="First Album", release_date=album_release_date, artist_id=artist.artist_id)
    print("Добавлен альбом:", album)

    print("\nДобавление песни...")
    song = add_song(title="Hit Song", duration=180, album_id=album.album_id)
    print("Добавлена песня:", song)

    # Получение данных
    print("\nПолучение всех артистов...")
    artists = get_all_artists()
    print("Все артисты:", artists)

    print(f"\nПолучение альбомов артиста {artist.name}...")
    albums = get_albums_by_artist(artist_id=artist.artist_id)
    print("Альбомы:", albums)

    print(f"\nПолучение песен альбома {album.title}...")
    songs = get_songs_by_album(album_id=album.album_id)
    print("Песни:", songs)

    print(f"\nПолучение полной информации об артисте {artist.name}...")
    full_info = get_artist_with_albums_and_songs(artist_id=artist.artist_id)
    print("Полная информация об артисте:")
    print(full_info)

if __name__ == "__main__":
    main()
