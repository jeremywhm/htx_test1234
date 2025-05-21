#!/usr/bin/env python3

# This file runs the ping API server.

import uvicorn


# Start the API server.
uvicorn.run("ping_api:app", port=8001)
