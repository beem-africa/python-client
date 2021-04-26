from BeemAfrica import secured, get_token


@secured
def magic():
    print("Hello")
    print(get_token())
