from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()


class OperationRequest(BaseModel):
    a: int
    b: int
    operator: str


def _calculate(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "^":
        return a**b
    if operator == "/":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        return a / b
    if operator == "//":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        return a // b
    if operator == "%":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        return a % b
    raise HTTPException(status_code=400, detail="Unknown operator")


@app.get("/healthz", response_model=dict)
def healthcheck():
    return {"status": "OK"}


@app.post("/", response_model=dict)
def calculate(request: OperationRequest):
    return {"result": _calculate(request.a, request.b, request.operator)}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
