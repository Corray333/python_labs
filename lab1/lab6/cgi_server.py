#!/usr/bin/env python3

import cgi
import cgitb
import json
from xml.etree import ElementTree as ET
from domain import session, Artist, Album, Song, add_artist, add_album, add_song

cgitb.enable()  # Для отладки

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

action = form.getvalue("action", "")

if action == "export":
    table = form.getvalue("table")
    fmt = form.getvalue("format", "json")
    if table == "artist":
        data = session.query(Artist).all()
    elif table == "album":
        data = session.query(Album).all()
    elif table == "song":
        data = session.query(Song).all()
    else:
        print("Invalid table")
        exit()

    if fmt == "json":
        print(json.dumps([obj.__dict__ for obj in data], default=str))
    elif fmt == "xml":
        root = ET.Element(table + "s")
        for obj in data:
            item = ET.SubElement(root, table)
            for key, value in obj.__dict__.items():
                if not key.startswith("_"):
                    ET.SubElement(item, key).text = str(value)
        print(ET.tostring(root, encoding="unicode"))
elif action == "import":
    table = form.getvalue("table")
    fmt = form.getvalue("format", "json")
    data = form.getvalue("data")
    if not data:
        print("No data provided")
        exit()

    if fmt == "json":
        data = json.loads(data)
    elif fmt == "xml":
        root = ET.fromstring(data)
        data = [{child.tag: child.text for child in item} for item in root]
    else:
        print("Invalid format")
        exit()

    for item in data:
        if table == "artist":
            add_artist(item["name"], item["genre"], item["birth_date"])
        elif table == "album":
            add_album(item["title"], item["release_date"], item["artist_id"])
        elif table == "song":
            add_song(item["title"], item["duration"], item["album_id"])
elif action == "add":
    table = form.getvalue("table")
    if table == "artist":
        add_artist(form.getvalue("name"), form.getvalue("genre"), form.getvalue("birth_date"))
    elif table == "album":
        add_album(form.getvalue("title"), form.getvalue("release_date"), form.getvalue("artist_id"))
    elif table == "song":
        add_song(form.getvalue("title"), form.getvalue("duration"), form.getvalue("album_id"))
else:
    print("Invalid action")
