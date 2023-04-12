# Imports
from fastapi import FastAPI

import uvicorn


# Application
app = FastAPI()


# Home endpoint
@app.get("/contratos", tags=["Contratos"])
def get_contratos():
    return {"message": "Welcome Contratos!"}


# Run application
if __name__ == "__main__":
    uvicorn.run("main:app", port=8010, reload=True)
    