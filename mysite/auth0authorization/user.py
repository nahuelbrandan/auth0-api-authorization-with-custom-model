from auth0authorization.backend import ApplicationBackend


def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')

    print '\n\n\nusername ', username

    aux = ApplicationBackend()
    aux.authenticate(username=username)

    return username
