#!/usr/bin/env python3

import uvicorn


uvicorn.run("ping_api:app", port=8001)
