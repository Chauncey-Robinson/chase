from fastapi import FastAPI

app = FastAPI()  # This is the "app" instance that Uvicorn is looking for

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chase API"}

