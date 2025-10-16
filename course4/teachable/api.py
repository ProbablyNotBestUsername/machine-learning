from keras.models import load_model, Model
from PIL import Image, ImageOps
import numpy as np
from io import BytesIO
from fastapi import FastAPI, UploadFile
from os.path import abspath
from typing import cast

np.set_printoptions(suppress=True)
model: Model = cast(Model, load_model(abspath("model/keras_Model.h5"), compile=False))
class_names = open(abspath("model/labels.txt"), "r").readlines()
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

app = FastAPI()

def predict_class(image_bytes):
    image = Image.open(BytesIO(image_bytes)).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name[2:].rstrip("\n"), confidence_score

@app.post("/predict")
async def post_pred_image(file: UploadFile):
    contents = await file.read()
    class_name, confidence = predict_class(contents)
    return {'class': class_name, 'confidence_score': float(confidence)}