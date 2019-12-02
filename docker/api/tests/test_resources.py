

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json['healthy'] == True


def test_words_index(client, word):
    resp = client.get('/words')
    assert resp.status_code == 200
    assert type(resp.json) == list
    assert resp.json[0].get('value') == word.value


def test_words_detail(client, word):
    resp = client.get(f'/words/{word.value}')
    assert resp.status_code == 200
    assert type(resp.json) == dict
    assert resp.json['value'] == word.value

    resp = client.get(f'/words/doesnotexist')
    assert resp.status_code == 404
    assert resp.content_type == "application/json"
