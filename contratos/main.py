# Imports
from fastapi import FastAPI

import uvicorn

from routers import front


# Application
app = FastAPI()


# Home endpoint
@app.get("/", tags=["Home"])
def Home():
    return {"message": "Welcome Home!"}


# Routers
app.include_router(front.router)


# Run application
if __name__ == "__main__":
    uvicorn.run("main:app", port=8010, reload=True)
