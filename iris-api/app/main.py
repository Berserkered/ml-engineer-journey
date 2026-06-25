from fastapi import FastAPI

from app.model import model
from app.schemas import PredictRequest, PredictResponse, HealthResponse

app = FastAPI(title="Iris Classifier", version="1.0.0")

@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    result = model.predict(request.to_features())
    return PredictResponse(**result)