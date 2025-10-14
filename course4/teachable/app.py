from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from io import BytesIO
import streamlit as st
import os

os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

image = None

def main():
    st.title('Модель предсказания')

    tab1, tab2 = st.tabs(["Предсказание", "Руководство"])

    with tab1:
        image = st.camera_input("Test")
        if image is not None:
            st.image(image)


        if st.button('Предсказать'):
            if image is None:
                return
            
            np.set_printoptions(suppress=True)
            model = load_model(os.path.abspath("model/keras_Model.h5"), compile=False)
            class_names = open(os.path.abspath("model/labels.txt"), "r").readlines()
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            size = (224, 224)



            image_bytes = image.getvalue()
            image = Image.open(BytesIO(image_bytes)).convert("RGB")

            # resizing the image to be at least 224x224 and then cropping from the center
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

            # turn the image into a numpy array
            image_array = np.asarray(image)

            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

            # Load the image into the array
            data[0] = normalized_image_array

            # Predicts the model
            prediction = model.predict(data)
            index = np.argmax(prediction)
            class_name = class_names[index]
            confidence_score = prediction[0][index]

            # Print prediction and confidence score
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", confidence_score)

            st.write("Class:", class_name[2:])
            st.write("Confidence Score:", confidence_score)

            # data = {
            #     "image": image
            # }

            # url = "http://127.0.0.1:8000/predict"
            # response = requests.post(url, json=data)
            # result = response.json()
            # clust = result.get("cluster")

            # st.markdown(f"""
            #             #### Предсказаный кластер
            #             """)
            # st.write(f"Название кластера: {clust[0]}")
            # st.write(f"{clust[1]}")
            # st.write("disabled")

        with tab2:
            tab2.subheader("Руководство пользователя")
            
            st.markdown(f"""
                        ### Как использовать программу:\n
                        **1.** Сделайте фото.\n
                        **2.** Программа\n
                        """)
        
if __name__ == "__main__":
    main()