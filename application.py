"""Modulo com as funcoes para CRUD no FCM."""

import logging

from fcm_phones import FCMApp

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

phone_number = '+5511968107055'

logging.info('Autenticando com o firebase...')

app = FCMApp()
user = app.authenticate()

logging.info(f'Autenticado, token obtido {user["idToken"]}')

logging.info('Conectando com o banco de dados...')

db = app.get_database()

logging.info('Conectado...')

logging.info(f'Recuperando os dados do celular com número {phone_number}')

phones = db.child('celulares').order_by_key().equal_to(phone_number).get().val()

logging.info('Phones: {}'.format(phones))

logging.info('Fim da execução...')
