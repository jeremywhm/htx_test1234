#!/usr/bin/env python3

# This file runs the ASR API server.

import uvicorn


# Start the API server.
uvicorn.run("asr_api:app", port=8002)
