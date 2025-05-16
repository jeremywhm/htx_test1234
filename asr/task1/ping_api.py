#!/usr/bin/env python3

from fastapi import FastAPI


app = FastAPI()

@app.get("/ping")
def pong():
    return "pong"
    