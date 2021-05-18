import asyncio
import falcon
import falcon.asgi

class Async:

    async def on_get(self, req, resp):
        await asyncio.sleep(1)
        resp.text = "Hello"
        resp.status = falcon.HTTP_200


app = falcon.asgi.App()
app.add_route("/async-txt", Async())

application = app
