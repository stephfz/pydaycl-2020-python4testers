import json
import requests

class BookingService(object):

    def __init__(self, base_url, service):
        self.header = {'cache-control': "no-cache"}
        self.base_url = base_url
        self.service_url = service

    def get_booking(self, boookingid):
        r = requests.get("{0}/{1}/{2}".format(self.base_url,
                                                self.service_url, boookingid))
        return r

    def new_booking(self, booking_data):
        self.header['Content-Type'] = "application/json"
        url = "{0}/{1}".format(self.base_url, self.service_url)
        payload = json.dumps(booking_data)
        r = requests.post(url, data = payload, headers=self.header)
        return r

    def update_booking(self, booking_data, bookingid, token):
        self.header['cookie'] = "token={0}".format(token)
        payload = json.dumps(booking_data)
        r = requests.put("{0}/{1}/{2}".format(self.base_url,
                                                self.service_url, bookingid),
                                    data = payload, headers=self.header)
        return r
