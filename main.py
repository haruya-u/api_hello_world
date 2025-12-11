from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_index() -> str:
    return """
    <html>
      <head>
        <title>FastAPI Hello</title>
      </head>
      <body>
        <h1>Welcome</h1>
        <p>Open the interactive API docs at http://URL/docs.</p>
      </body>
    </html>
    """


@app.get("/hello_world")
async def read_root() -> dict[str, str]:
    return {"message": "hello world! Updated from the browser!"}
