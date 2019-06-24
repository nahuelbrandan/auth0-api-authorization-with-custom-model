from django.contrib.auth import authenticate

from auth0authorization.backend import MyCustomBackend


def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')

    # este es la funcion que estaba originalmente.
    # ver https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/backends/#ModelBackend.authenticate
    asd = authenticate(remote_user=username)

    # aux = MyCustomBackend()
    # obj = aux.authenticate(username=username)

    print 'username', username, type(username)
    print 'asd', asd, type(asd)
    # print 'aux', aux, type(aux)
    # print 'obj', obj, type(obj)
    return username
