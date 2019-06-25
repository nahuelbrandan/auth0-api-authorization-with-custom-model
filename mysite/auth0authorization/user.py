from auth0authorization.backend import MyCustomBackend


def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')

    aux = MyCustomBackend()
    aux.authenticate(username=username)

    return username
