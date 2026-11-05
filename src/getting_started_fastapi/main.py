from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from Server!!"}


@app.get("/health")
def healthcheck():
    return {"status": "healthy"}
