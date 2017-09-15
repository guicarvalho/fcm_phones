"""Modulo com as configuracoes do projeto."""

import os

import pyrebase

config = {
    'apiKey': 'AIzaSyDf--VwfsmHSnKNtiyQuPYVf2KDCUlqpsw',
    'authDomain': 'fc-phones-0.firebaseapp.com',
    'databaseURL': 'https://fc-phones-0.firebaseio.com',
    'storageBucket': 'fc-phones-0.appspot.com',
}

EMAIL = os.getenv('GMAIL_USER', 'user@gmail.com')
PASSWD = os.getenv('GMAIL_PASSWD', '1234')

