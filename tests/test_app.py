# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

def test_get_list(db_connection, web_client):
    db_connection.seed("seeds/music_web.sql")
    response = web_client.get("/list")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        'Album(1, Doolittle, 1989, 1)',
        'Album(2, Surfer Rosa, 1988, 1)',
        'Album(3, Waterloo, 1974, 2)',
        'Album(4, Super Trouper, 1980, 2)',
        'Album(5, Bossanova, 1990, 1)',
        'Album(6, Lover, 2019, 3)',
        'Album(7, Folklore, 2020, 3)',
        'Album(8, I Put a Spell on You, 1965, 4)',
        'Album(9, Baltimore, 1978, 4)',
        'Album(10, Here Comes the Sun, 1971, 4)',
        'Album(11, Fodder on My Wings, 1982, 4)',
        'Album(12, Ring Ring, 1973, 2)'
        ])
def test_if_album_was_added(db_connection, web_client):
    db_connection.seed("seeds/music_web.sql")

    response = web_client.post("/albums", data={
        "title": "Voyage",
        "release_year": 2022,
        "artist_id": 2})

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album added successfully"

    response = web_client.get("/list")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        'Album(1, Doolittle, 1989, 1)',
        'Album(2, Surfer Rosa, 1988, 1)',
        'Album(3, Waterloo, 1974, 2)',
        'Album(4, Super Trouper, 1980, 2)',
        'Album(5, Bossanova, 1990, 1)',
        'Album(6, Lover, 2019, 3)',
        'Album(7, Folklore, 2020, 3)',
        'Album(8, I Put a Spell on You, 1965, 4)',
        'Album(9, Baltimore, 1978, 4)',
        'Album(10, Here Comes the Sun, 1971, 4)',
        'Album(11, Fodder on My Wings, 1982, 4)',
        'Album(12, Ring Ring, 1973, 2)',
        'Album(13, Voyage, 2022, 2)'
        ])
    
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_web.sql")
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        'Artist(1, Pixies, Rock)',
        'Artist(2, ABBA, Pop)',
        'Artist(3, Taylor Swift, Pop)',
        'Artist(4, Nina Simone, Jazz)'
        ])

def test_if_artist_was_added(db_connection, web_client):
    db_connection.seed("seeds/music_web.sql")

    response = web_client.post("/add", data={
        "name": "Wild Nothing",
        "genre": "Indie"})

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Artist added successfully"

    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        'Artist(1, Pixies, Rock)',
        'Artist(2, ABBA, Pop)',
        'Artist(3, Taylor Swift, Pop)',
        'Artist(4, Nina Simone, Jazz)',
        'Artist(5, Wild Nothing, Indie)'
        ])