import uvicorn
from fastapi import FastAPI

app = FastAPI()
app.include_router(user)

if __name__ == "__main__":
   uvicorn.run("index:app", host="127.0.0.1", port=8050,reload = True)
   


