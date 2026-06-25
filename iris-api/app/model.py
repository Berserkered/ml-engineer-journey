from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).parent.parent / "model.joblib"

class IrisModel:
    def __init__(self, path: Path = MODEL_PATH) -> None:
        artifact = joblib.load(path)
        self._model = artifact["model"]
        self._target_names = artifact["target_names"]
        
    def predict(self, features: list[float]) -> dict:
        pred = self._model.predict([features])[0]
        proba = self._model.predict_proba([features])[0]
        return {
            "label": self._target_names[pred],
            "class_id": int(pred),
            "confidence": float(proba[pred]),
        }
    
model = IrisModel()