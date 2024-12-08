from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artist'
    artist_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)

    albums = relationship("Album", back_populates="artist")

    def __repr__(self):
        return f"<Artist(name='{self.name}', genre='{self.genre}', birth_date='{self.birth_date}')>"

class Album(Base):
    __tablename__ = 'album'
    album_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    artist_id = Column(Integer, ForeignKey('artist.artist_id'), nullable=False)

    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album")

    def __repr__(self):
        return f"<Album(title='{self.title}', release_date='{self.release_date}')>"

class Song(Base):
    __tablename__ = 'song'
    song_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    album_id = Column(Integer, ForeignKey('album.album_id'), nullable=False)

    album = relationship("Album", back_populates="songs")

    def __repr__(self):
        return f"<Song(title='{self.title}', duration={self.duration})>"

DATABASE_URL = "sqlite:///music.db"  
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

def add_artist(name, genre, birth_date):
    artist = Artist(name=name, genre=genre, birth_date=birth_date)
    session.add(artist)
    session.commit()
    return artist

def get_all_artists():
    return session.query(Artist).all()

def add_album(title, release_date, artist_id):
    album = Album(title=title, release_date=release_date, artist_id=artist_id)
    session.add(album)
    session.commit()
    return album

def get_albums_by_artist(artist_id):
    return session.query(Album).filter_by(artist_id=artist_id).all()

def add_song(title, duration, album_id):
    song = Song(title=title, duration=duration, album_id=album_id)
    session.add(song)
    session.commit()
    return song

def get_songs_by_album(album_id):
    return session.query(Song).filter_by(album_id=album_id).all()

def get_artist_with_albums_and_songs(artist_id):
    artist = session.query(Artist).filter_by(artist_id=artist_id).first()
    if artist:
        return {
            "artist": artist,
            "albums": [
                {
                    "album": album,
                    "songs": album.songs
                } for album in artist.albums
            ]
        }
    return None
