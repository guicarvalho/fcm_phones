"""Modulo para criar objeto da aplicaao."""

import pyrebase

from fc_phones import config


class FCMApp:
    """Classe com os metodos para gerenciar o FCM."""

    def __init__(self):
        """Construtor."""
        self._app = pyrebase.initialize_app(config.config)
        self._auth = self._app.auth()
        self._user = None

    def authenticate(self):
        """Autentica no FCM."""
        self._user = self._auth.sign_in_with_email_and_password(
            config.EMAIL, config.PASSWD)
        return self._user

    def refresh_token(self):
        """Atualiza o token."""
        user = self._user()
        self._user = self._auth.refresh(user['idToken'])
        return self._user

    def get_database(self):
        """Recupera instancia para BD."""
        return self._app.database()
