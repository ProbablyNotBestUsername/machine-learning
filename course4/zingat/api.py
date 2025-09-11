from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import numpy as np

app = FastAPI()

with open('./bag_regressor.pkl', 'rb') as f:
    bag_reg = pickle.load(f)

class RegInput(BaseModel):
    features: list[float]

@app.post("/predict")
def predict_price(inp: RegInput):
    x = np.array(inp.features).reshape(1, -1)
    print(bag_reg.predict(x))
    return {"predicted_price": float(bag_reg.predict(x)[0])}