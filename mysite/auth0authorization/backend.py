from auth0authorization.models import CustomUser


class MyCustomBackend:
    def __init__(self):
        pass

    def authenticate(self, username=None):
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            user = CustomUser.objects.create(username=username)
        return user

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
