

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json['data']['healthy'] == True


def test_words_index(client, word):
    resp = client.get('/words')
    assert resp.status_code == 200
    assert type(resp.json['data']) == list
    assert resp.json['data'][0].get('id') == word.id
    assert resp.json['data'][0].get('definition') == word.definition


def test_words_detail(client, word):
    resp = client.get(f'/words/{word.id}')
    assert resp.status_code == 200
    assert type(resp.json) == dict
    assert resp.json['data']['id'] == word.id
    assert resp.json['data']['definition'] == word.definition

    resp = client.get(f'/words/doesnotexist')
    assert resp.status_code == 404
    assert resp.content_type == "application/json"


def test_words_starting_with(client, word):
    resp = client.get('/words/starting-with/SC')
    assert resp.status_code == 200
    assert resp.json['data'][0]['id'] == word.id


def test_words_ending_with(client, word):
    resp = client.get('/words/ending-with/LE')
    assert resp.status_code == 200
    assert resp.json['data'][0]['id'] == word.id


def test_words_ending_with(client, word):
    resp = client.get('/words/containing/BL')
    assert resp.status_code == 200
    assert resp.json['data'][0]['id'] == word.id
