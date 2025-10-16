import streamlit as st
import os
import requests

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
                st.error("Сделайте фото для предсказания.")
                return

            data = {
                "file": image.getvalue()
            }

            try:
                url = "http://127.0.0.1:8000/predict"
                response = requests.post(url, files=data)
            except ConnectionError:
                st.error("API не отвечает. Убедитесь, что API запущен.")
                return
            result = response.json()
            class_name = result.get("class")
            score = result.get("confidence_score")

            st.markdown(f"""
                        #### Предсказаный класс: {class_name}
                        """)
            st.write(f"Точность: {score * 100:.2f}%")

        with tab2:
            tab2.subheader("Руководство пользователя")
            
            st.markdown(f"""
                        ### Как использовать программу:\n
                        **1.** Сделайте фото.\n
                        **2.** Программа автоматически определит класс изображения и выведет результат.\n
                        """)
        
if __name__ == "__main__":
    main()