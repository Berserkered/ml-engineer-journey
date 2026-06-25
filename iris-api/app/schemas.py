from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    sepal_length: float = Field(..., gt=0, description="cm")
    sepal_width: float = Field(..., gt=0, description="cm")
    petal_length: float = Field(..., gt=0, description="cm")
    petal_width: float = Field(..., gt=0, description="cm")
    
    def to_features(self) -> list[float]:
        return [self.sepal_length, self.sepal_width, self.petal_length, self.petal_width]
    
class PredictResponse(BaseModel):
    label: str
    class_id: int
    confidence: float
    
class HealthResponse(BaseModel):
    status: str