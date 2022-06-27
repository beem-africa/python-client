
import sys
import requests
from BeemAfrica import secured, get_header


BASE_OTP_URL = 'https://apiotp.beem.africa/v1/request'
BASE_VERIFY_URL = 'https://apiotp.beem.africa/v1/verify'


class OTP(object):
    def __init__(self):
        pass

    @secured
    def send_otp(self, recipient=None, app_id=None) -> dict:
        if not recipient:
            raise ValueError('recipient number should not be empty')
        
        if not app_id:
            raise ValueError('App ID should not be empty, this is your Beem App ID')

        if not isinstance(app_id, int):
            raise TypeError(
                f'app_id should be of type <str> not {type(app_id)}')

        if not isinstance(recipient, str):
            raise TypeError(
                f'recipient number should be of type<str> not {type(recipient)}')

        try:
            return requests.post(
                BASE_OTP_URL,
                headers=get_header(),
                json={
                    'msisdn': recipient,
                    'appId': app_id
                }
            ).json()

        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError(
                'Connection to Beem OTP API Refused, Please check your internet connections')

    @secured
    def verify(self, pin_id: str, pin: str) -> dict:
        if not all([isinstance(pin_id, str), isinstance(pin, str)]):
            raise TypeError('Both pin_id and pin should be of type<str>')

        try:
            return requests.post(
                BASE_VERIFY_URL,
                headers=get_header(),
                json={
                    'pinId': pin_id,
                    'pin': pin
                }
            ).json()
        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError(
                'Connection to Beem Verify OTP API Refused, Please check your connections')


sys.modules[__name__] = OTP()
