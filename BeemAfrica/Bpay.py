import sys
import requests
from BeemAfrica import secured, get_header

BPAY_BALANCE_URL = "https://apitopup.beem.africa/v1/credit-balance?app_name={}"
BPAY_CHECKOUT_URL = "https://checkout.beem.africa/v1/checkout"


class Bpay(object):
    def __init__(self) -> None:
        super().__init__()

    @secured
    def get_balance(self, app_name="USSD"):
        try:
            return requests.get(
                BPAY_BALANCE_URL.format(app_name), headers=get_header()
            ).json()

        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError(
                "Connection to the USSD Get balance API Refused, Please check your internet connections"
            )

    @secured
    def checkout(
        self,
        amount: int = None,
        reference_number: str = None,
        mobile: str = None,
        transaction_id: str = None,
        sendSource: bool = True,
    ):
        """
        QUERY
            Field	Type	Description
            amount	string
            The amount that the customer has to pay, Decimals not allowed

            transaction_id	string
            Transaction ID to track the payment. Should be UUIDv4. E.g. 96f9cc09-afa0-40cf-928a-d7e2b27b2408

            reference_number	string
            Reference number to track the payment. Should be alphanumeric.The prefix pattern should be added when creating collections & checkout products. Example: SAMPLE-12345

            mobile optional	string
            Mobile Number with country code prefix e.g. 255701000000

            sendSource optional	boolean
            If set to true, response will be a SRC redirect link (recommended if redirect is handled from backend)
            If set to false, response will be a redirection with code 302 (recommended if redirect is handled from the front)
        """
        params = {
            "amount": amount,
            "reference_number": reference_number,
            "mobile": mobile,
            "sendSource": sendSource,
            "transaction_id": transaction_id,
        }
        try:
            return requests.get(
                BPAY_CHECKOUT_URL, params=params, headers=get_header()
            ).json()

        except (requests.ConnectionError, requests.ConnectTimeout):
            raise ConnectionError(
                "Connection to the BPay checkout, Please check your internet connections"
            )


sys.modules[__name__] = Bpay()
