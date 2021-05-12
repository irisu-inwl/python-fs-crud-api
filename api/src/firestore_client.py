import os

from mockfirestore import MockFirestore
from google.cloud import firestore


def get_fs_client(config: str):
    if config == 'local':
        fs = MockFirestore()
    else:
        fs = firestore.Client()
    
    return fs


config = os.getenv('APP_CONFIG')
fs = get_fs_client(config)
