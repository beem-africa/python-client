import sys
import requests
from BeemAfrica import secured, get_header

TWOWAYSMS_BALANCE_URL = 'https://www.blsmsgw.com/portal/api/userAccountBalance'


class TwowaySMS(object):
    def __init__(self) -> None:
        super().__init__()

    @secured
    def get_balance(self):
        try:
            return requests.get(
                TWOWAYSMS_BALANCE_URL,
                headers=get_header()
            ).json()

        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError(
                'Connection to the USSD Get balance API Refused, Please check your internet connections')


sys.modules[__name__] = TwowaySMS()
