import os

from mockfirestore import MockFirestore
from google.cloud import firestore


def get_fs_client(config: str, project_id: str):
    if config == 'local':
        fs = MockFirestore()
    else:
        fs = firestore.Client(project=project_id)
    
    return fs


project_id = os.getenv('PROJECT_ID')
config = os.getenv('APP_CONFIG')
fs = get_fs_client(config, project_id)
