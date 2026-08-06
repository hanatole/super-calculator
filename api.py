from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz", response_model=dict)
def healthcheck():
    return {"status": "OK"}
