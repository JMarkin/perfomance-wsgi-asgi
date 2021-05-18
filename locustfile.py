from locust import task
from locust.contrib.fasthttp import FastHttpUser

class Async(FastHttpUser):

    @task
    def async_root(self):
        self.client.get("/async-txt")


class Sync(FastHttpUser):

    @task
    def sync_root(self):
        self.client.get("/sync-txt")
