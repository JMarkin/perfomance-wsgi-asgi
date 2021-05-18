import time
import asyncio
import falcon


class Sync:

    def on_get(self, req, resp):
        time.sleep(1)
        resp.text = "Hello"
        resp.status = falcon.HTTP_200


app = falcon.App()
app.add_route("/sync-txt", Sync())

application = app
