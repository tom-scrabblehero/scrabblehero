

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json['healthy'] == True


def test_words_index(client, word):
    resp = client.get('/words')
    assert resp.status_code == 200
    assert type(resp.json) == list
    assert resp.json[0].get('value') == word.value
