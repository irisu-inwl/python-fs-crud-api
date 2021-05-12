import time
from uuid import uuid4
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    def initialize_task(self):
        self.collection_id = uuid4()
        self.doc_id = uuid4()

    def get_fs(self):
        uri = f'/fs/{self.collection_id}/{self.doc_id}'
        self.client.get(uri, name='get_fs')

    def post_fs(self):
        uri = f'/fs/{self.collection_id}/{self.doc_id}'
        headers = {'content-type': 'application/json'}
        payload = {'key': 'value'}
        self.client.post(uri, json=payload, headers=headers, name='post_fs')

    def put_fs(self):
        uri = f'/fs/{self.collection_id}/{self.doc_id}'
        headers = {'content-type': 'application/json'}
        payload = {'key': 'updated'}
        self.client.put(uri, json=payload, headers=headers, name='put_fs')

    def delete_fs(self):
        uri = f'/fs/{self.collection_id}/{self.doc_id}'
        self.client.delete(uri, name='delete_fs')

    @task
    def normal_scenario(self):
        self.initialize_task()
        self.post_fs()
        self.get_fs()
        self.put_fs()
        self.delete_fs()
