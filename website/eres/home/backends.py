from . models import Usuario

class UsuarioAuthBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            usuario = Usuario.objects.get(username=username)

            if password == usuario.password:
                # Authentication success by returning the user
                return usuario
            else:
                # Authentication fails if None is returned
                return None

        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
