import sys
import json
import requests
from base64 import b64encode
from typing import Union, List
from BeemAfrica import secured, get_header


BASE_SMS_URL = 'https://apisms.beem.africa/v1/send'
BASE_BALANCE_URL = 'https://apisms.beem.africa/v1/vendors/balance?vendor_id={}'


class SMS(object):
    def __init__(self) -> None:
        super().__init__()
        self.sender_id = 'INFO'
        self.schedule_time = ''

    @secured
    def send_sms(self, message: str, recipients, **extra_details):
        try:
            r_body = self.get_body(message, recipients, **extra_details)
            return requests.post(
                BASE_SMS_URL,
                headers=get_header(),
                json=r_body
            ).json()
        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError(
                "Connection to Beem SMS API Refused Please check your internt connections")

    def get_balance(self, sender_id: str = None):
        if not sender_id:
            sender_id = self.sender_id

        try:
            print(sender_id)
            return requests.post(
                BASE_BALANCE_URL.format(sender_id),
                headers=get_header()
            ).json()

        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError(
                "Connection Refused , Please check your internt connections")

    def get_body(self, message, recipients, **extra_details):
        if not isinstance(recipients, (list, str)):
            raise TypeError(
                f'recipients should be of Either type <list> or type <str> but not {type(recipients)} ')

        if isinstance(recipients, list):
            recipients = [{'recipient_id': index+1, 'dest_addr': recipient}
                          for index, recipient in enumerate(recipients)]

        if isinstance(recipients, str):
            recipients = [{
                'recipient_id': 1,
                'dest_addr': recipients
            }]

        return {
            'source_addr': extra_details.get('sender_id', self.sender_id),
            'schedule_time': extra_details.get('schedule_time', self.schedule_time),
            'encoding': 0,
            'message': message,
            'recipients': recipients

        }


sys.modules[__name__] = SMS()
