# Imports
from fastapi import FastAPI

import uvicorn


# Application
app = FastAPI()


# Home endpoint
@app.get("/admin", tags=["Admin"])
def get_admin():
    return {"message": "Welcome Admin!"}


# Run application
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
    