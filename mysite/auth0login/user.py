from django.contrib.auth import authenticate

from auth0login.backend import MyCustomBackend


def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')

    # este es la funcion que estaba originalmente.
    # ver https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/backends/#ModelBackend.authenticate
    # authenticate(remote_user=username)

    aux = MyCustomBackend()
    aux.authenticate(username=username)

    return username
