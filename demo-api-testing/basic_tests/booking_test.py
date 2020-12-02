import requests

def test_get_existing_booking():
    response = requests.get("https://restful-booker.herokuapp.com/booking/1")
    assert response.status_code == 200
