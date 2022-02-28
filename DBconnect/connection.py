from pymongo import MongoClient
from typing import Optional
# from Models.job_model import jobs
# from Credentials.credentials import Mongodb
import DBconnect.credentials as c



url = "mongodb+srv://"+c.Mongodb['Username']+":"+c.Mongodb['Pass']+"@jobs.uloew.mongodb.net/Jobs?retryWrites=true&w=majority"

client = MongoClient(url)
db = client.Job_Database
mycol = db.Jobs

async def create_job(job):
    document = job
    result = mycol.insert_one(document)
    return document

async def create_many_jobs(job):
    document = job
    temp = []
    for i in range(0,len(document)):
        temp.append(document[i].dict())
    result = mycol.insert_many(temp)
    return document



