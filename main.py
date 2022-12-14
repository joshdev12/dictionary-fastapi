import os
import json
import uvicorn
from fastapi import FastAPI

app = FastAPI()

with open("dictionary.json", mode="r") as file:
    dictionary = json.load(file)

@app.get("/")
def dictionary_list():
    return dictionary


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")