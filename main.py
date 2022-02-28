from typing import Optional,List,Dict
from urllib import response
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from DBconnect.connection import create_job,create_many_jobs
from Models.job_model import jobs
from scraper import linkedin_api
from beauty import beautifer
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/linkedin_data")
# async def get_data():
#     list_data = beautifer()
#     data = list_data[1]
#     print(data)
#     r = requests.post(url = 'http://127.0.0.1:8000/api/job', data = data)
#     return r
    


# @app.get("/api/job{id}")
# async def get_job_by_id(id):
#     return 1


@app.post("/api/job", response_model=jobs)
async def post_job(job:jobs):
    response = await create_job(job.dict())
    if response:
        return response
    raise HTTPException(400,"SMH")


@app.post("/api/job1")
async def post_many_job(many_job:List[jobs]):
    response = await create_many_jobs(many_job)
    if response:
        return response
    raise HTTPException(400,"smh")
    # response = await create_many_jobs(job.dict())
    # if response:
    #     return response
    # raise HTTPException(400,"SMH")


# @app.put("/api/job{id}")
# async def put_job(id, data):
#     return 1

# @app.delete("/api/job{id}")
# async def delete_job(id):
#     return 1



# @app.("ins_rec/{Company_name}")
# def insert_record(Company_name:str, role:Optional[str]=None, location:Optional[str]=None, jtype:Optional[str]=None):
#     record_dict = dict()
#     record_dict = {
#         "Company": Company_name,
#         "Role": role,
#         "Location": location,
#         "Type": jtype
#         }
#     connection.mydb.mycol.insert_one(record_dict)
