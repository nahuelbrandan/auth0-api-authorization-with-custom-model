from auth0authorization.models import Application


class ApplicationBackend:
    def __init__(self):
        pass

    def authenticate(self, username=None):
        try:
            user = Application.objects.get(username=username)
        except Application.DoesNotExist:
            user = Application.objects.create(username=username)
        return user

    def get_user(self, user_id):
        try:
            return Application.objects.get(pk=user_id)
        except Application.DoesNotExist:
            return None
