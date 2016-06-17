from . models import Usuario
from . models import tiposDeUsuario
from django.contrib.auth.models import User


class CustomUserAuth(object):

    def authenticate(self, username=None, password=None):
        try:
            usuario = Usuario.objects.get(username=username)

            if password == usuario.password:
                # Authentication success by returning the user
                try:
                    user = User.objects.get(username=username)
                    return user
                except User.DoesNotExist:
                    user = User(username=username, password=password)
                    if usuario.tipoUsuario == tiposDeUsuario['gerente']:
                        user.is_staff = True
                        user.is_superuser = True
                    else:
                        user.is_staff = False
                        user.is_superuser = False
                    user.is_active = True
                    user.save()
                    return user
            else:
                # Authentication fails if None is returned
                return None

        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
