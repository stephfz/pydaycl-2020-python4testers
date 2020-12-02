import json
import pytest

from booking_service import BookingService
from authorization_service import AuthorizationService

from data_services import DataProvider

BASE_URL = "https://restful-booker.herokuapp.com"
booking_service = BookingService(BASE_URL, 'booking')
data_services = DataProvider()


def test_get_existing_booking():
    r = booking_service.get_booking(1)
    assert r.status_code == 200

def test_get_non_existing_booking():
    r = booking_service.get_booking(34541)
    assert r.status_code == 404

def test_create_new_booking_sucessful():
    booking_data = data_services.new_booking_data()
    r = booking_service.new_booking(booking_data)
    assert r.status_code == 200

def test_update_booking():
    booking_data = data_services.new_booking_data()
    r = booking_service.new_booking(booking_data)
    assert r.status_code == 200
    bookingid = r.json()["bookingid"]
    print (bookingid)
    # get authorization
    auth_service = AuthorizationService(BASE_URL, 'auth')
    authorization = auth_service.authorize_user('admin', 'password123')
    token = authorization.json()["token"]
    #update
    new_need = 'Non-Smooking Room'
    booking_data['additionalneeds'] = new_need
    r = booking_service.update_booking(booking_data,
                                    bookingid, token = token)
    assert r.status_code == 200
    assert r.json()['additionalneeds'] == new_need
