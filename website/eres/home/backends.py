from .models import Usuario

class UsuarioAuthBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            usuario = Usuario.objects.get(username=username)

            if usuario.password == password:

                return usuario
            else:
                return None

        except User.DoesNotExist:
            return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
