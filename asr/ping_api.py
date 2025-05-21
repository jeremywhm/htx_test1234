#!/usr/bin/env python3

# This file defines the ping API.

from fastapi import FastAPI


app = FastAPI()

@app.get("/ping")
def pong():
    # Return pong when called.
    return "pong"
    