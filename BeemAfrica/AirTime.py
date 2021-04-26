import sys
import requests
from BeemAfrica import secured, get_header


# The Beem Airtime Topup service allows customers to be ableto send airtime credit
# directly to any mobile number on supported networks via web and API.

TRANSFER_AIRTIME_URL = 'https://apiairtime.beem.africa/v1/transfer'
AIRTIME_BALANCE_URL = 'https://apitopup.beem.africa/v1/credit-balance?app_name={}'


class AirTime(object):
    def __init__(self) -> None:
        super().__init__()

    @secured
    def transfer_airtime(self, recipient: str, amount: float) -> dict:
        if not isinstance(recipient, str):
            raise TypeError(
                f'recipient number should be of type<str> not {type(recipient)}')

        if not isinstance(amount, (int, float)):
            raise TypeError(
                f'amount should either be of type<int> or type<float> but not {type(amount)}')
        try:
            return requests.post(
                TRANSFER_AIRTIME_URL,
                headers=get_header(),
                json={
                    'dest_addr': recipient,
                    'amount': amount
                }
            ).json()

        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError(
                'Connection to Beem Transfer Airtime API refused, please check your internet connection')

    @secured
    def get_credit_balance(self, app_name='AIRTIME'):
        try:
            return requests.get(
                AIRTIME_BALANCE_URL.format(app_name),
                headers=get_header(),
            ).json()
        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError(
                'Connection to Beem Get credit balance API refused, please check your internet connection')


sys.modules[__name__] = AirTime()
