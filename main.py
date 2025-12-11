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

from datetime import datetime
@app.get("/current_time")
async def get_current_time() -> dict[str, str]:
    now = datetime.now()
    return {"current_time": now.strftime("%Y-%m-%d %H:%M:%S"),"timezone": "Asia/Tokyo"
           }

from datetime import datetime
@app.get("/greet/{name}")
async def greet_user(name: str) -> dict[str, str]:
    return {"message": f" {name} ","timestamp": datetime.now().strftime("%H:%M:%S")
           }
    @app.get("/double/{number}")


    
async def double_number(number: int) -> dict[str, int]:
    return {"input": number,"result": number * 2
           }

import random
@app.get("/random_quote")
async def get_random_quote() -> dict[str, str]:
    quotes = ["失敗は成功のもと "," 継続は力なり"," 千里の道も一歩から"," 七転び八起き"
             ]
    return {"quote": random.choice(quotes)}




