
def test_app(app):
    assert app.config['TESTING'] == True
