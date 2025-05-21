#!/usr/bin/env python3

# This file runs the ASR API server.

import uvicorn


# Start the API server.
uvicorn.run("asr_api:app", host="0.0.0.0", port=8001)
