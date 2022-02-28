
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from scraper import linkedin_api
from beauty import beautifer
import requests
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/linkedin_data")
async def get_data():
    list_data = linkedin_api()
    r = requests.post(url = 'http://127.0.0.1:8000/api/job1', json = list_data)
    return {"Done"}

if __name__ == "__main__":
    uvicorn.run(app, port=5000)