# Imports
from fastapi import FastAPI

import uvicorn


# Application
app = FastAPI()


# Home endpoint
@app.get("/", tags=["Home"])
def get_home():
    return {"message": "Welcome Home!"}


# Run application
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
    