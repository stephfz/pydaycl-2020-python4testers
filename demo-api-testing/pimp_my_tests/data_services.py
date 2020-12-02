import os
import string
import random
import json

class DataProvider():

    def new_booking_data(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = '{0}/data_templates/new_booking.json'.format(dir_path)
        with open(file_path) as json_file:
            data = json.load(json_file)
        data['firstname'] = self.generate_random_string()
        data['lastname'] = self.generate_random_string()
        return data

    def generate_random_string(self, size=6, chars=string.ascii_letters):
        return ''.join(random.choice(chars) for _ in range(size))
