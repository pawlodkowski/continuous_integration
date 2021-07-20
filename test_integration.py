from bs4 import BeautifulSoup


# def test_integration(client):
#     """
#     Test if passing arguments via a get request results in a sensible result
#     """
#     response = client.get("/recommender?movie=Titanic&rating=5").data
#     soup = BeautifulSoup(response, "lxml")
#     result = soup.body.h2.next_sibling.next_sibling.find_all("li")
#     print(result)
#     assert len(result) == 3
