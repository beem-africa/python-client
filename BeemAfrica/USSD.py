import sys
import requests
from BeemAfrica import secured, get_header


USSD_BALANCE_URL = 'https://apitopup.beem.africa/v1/credit-balance?app_name={}'


class USSD(object):
    def __init__(self) -> None:
        super().__init__()

    @secured
    def get_balance(self, app_name='USSD'):
        try:
            return requests.get(
                USSD_BALANCE_URL.format(app_name),
                headers=get_header()
            ).json()

        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError(
                'Connection to the USSD Get balance API Refused, Please check your internet connections')


sys.modules[__name__] = USSD()
