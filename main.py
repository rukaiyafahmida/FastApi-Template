
from fastapi import FastAPI 
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from decouple import config



app = FastAPI(title="FastAPI Template")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"working" : "true"}
