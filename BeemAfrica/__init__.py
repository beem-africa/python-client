from base64 import b64encode
from functools import wraps
from dataclasses import dataclass


Tokens = ""


@dataclass
class Token(object):
    access_key: str = ""
    secret_key: str = ""
    beem_secure_token: str = ""


class Authorize(object):
    def __init__(
        self,
        access_key: str = None,
        secret_key: str = None,
        beem_secure_token: str = None,
    ):
        if not isinstance(access_key, str) or not isinstance(secret_key, str):
            raise TypeError("Both access_key and secret key should be of type <str>")
        self.token = Token(access_key, secret_key, beem_secure_token)
        globals()["Tokens"] = self.token

    @property
    def access_key(self) -> str:
        return self.token.access_key

    @access_key.setter
    def access_key(self, access_key: str):
        if not isinstance(access_key, str):
            raise TypeError(f"access_key should of Type <str> not {type(access_key)}")
        self.token.access_key = access_key

    @property
    def beem_secure_token(self) -> str:
        return self.token.beem_secure_token

    @beem_secure_token.setter
    def beem_secure_token(self, beem_secure_token: str):
        if not isinstance(beem_secure_token, str):
            raise TypeError(
                f"beem_secure_token should of Type <str> not {type(beem_secure_token)}"
            )
        self.token.beem_secure_token = beem_secure_token

    @property
    def secret_key(self) -> str:
        return self.token.secret_key

    @secret_key.setter
    def secret_key(self, secret_key: str):
        if not isinstance(secret_key, str):
            raise TypeError(
                f"secret_key should be of Type <str> not {type(secret_key)}"
            )
        self.token.secret_key = secret_key


def secured(beem_method):
    @wraps(beem_method)
    def verify(*args, **kwargs):
        _Tokens = globals()["Tokens"]
        if not isinstance(Tokens, Token) or not (
            _Tokens.access_key and _Tokens.secret_key
        ):
            raise ValueError(
                f"""
                You need to set the value of access_key and secret_key
                
                do this to setup !!!
                
                >>> from BeemAfrica import Authorize
                >>> Authorize(access_key, secret_key)
                 """
            )
        return beem_method(*args, **kwargs)

    return verify


def get_header():
    token = globals()["Tokens"]
    beem_secure_token = token.beem_secure_token
    encoded_token = b64encode(
        f"{token.access_key}:{token.secret_key}".encode()
    ).decode()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {encoded_token}",
    }
    if beem_secure_token:
        headers["beem_secure_token"] = beem_secure_token
    return headers
