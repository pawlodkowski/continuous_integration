"""
Contains the test cases for the application unit tests.
"""

# from application import app
# import requests


def test_homepage_available(client):
    """Test if we can access the homepage"""
    # 1. we need to run the web application
    # app.run(debug=True, port=5000)

    # 2. send a get request to the url http://127.0.0.1:5000/
    # response = requests.get("http://127.0.0.1:5000/")
    response = client.get("/")

    # 3. assert that the request was valid and served
    assert response.status_code == 200


def test_homepage_contains_convolutional(client):
    """Tests if the homepage contains the word convolutional"""
    response = client.get("/")
    assert "Convolutional" in response.data.decode("utf-8")
