def test_app():
    assert False

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    # assert b"Welcome to my Flask app!" in response.data