import streamlit as st
import requests
import os

os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

st.title('Предсказание цены')

tab1, tab2 = st.tabs(["Предсказание", "Руководство"])

with tab1:
    listing_type_text = st.selectbox("Тип объявления", options=["Резиденция", "Квартира", "Вилла", "Семейный дом", "Кооператив", "Летний дом", "Комплекс зданий", "Префабричный дом", "Дворец / Особняк", "Фермерский дом", "Квартира в особняке", "Лофт"])
    tom_input = st.number_input("Количество дней на сайте", min_value=0)
    building_age_input = st.number_input("Возраст здания", min_value=0)
    total_floor_count_input = st.number_input("Количество этажей в здании", min_value=0)
    floor_no_input = st.number_input("Этаж квартиры", min_value=0)
    room_count_input = st.selectbox("Количество комнат", options=["2+1", "1+0", "1+1", "2+0", "3+1", "4+1", "9+2", "5+2", "6+3", "6+2", "4+3", "9+5", "5+1", "3+2", "2+2", "4+2", "7+2", "9+4", "8+3", "8+1", "10+1", "10+0", "9+3", "8+4", "7+3", "10+2", "8+2", "7+1", "5+3", "9+1", "0+0", "10+3", "10+4", "11+3", "15+5"])
    size_input = st.number_input("Площадь квартиры (в м²)", min_value=0.0, format="%.2f")
    heating_type_input = st.selectbox("Тип отопления", options=["Фанкойл", "Отсутствует", "Отопление (природным газом)", "Отопление (углём)", "Комбинированный котел (электричеством)", "Кондиционер", "Комбинированный котел (природным газом)", "Центральное отопление (по счётчику тепла)", "Центральное отопление", "Угольная печь", "Тёплый пол", "Плитой (природный газ)", "Солнечная энергия", "Отопление (мазутом)", "Геотермальное отопление", "Подогрев пола"])



    if st.button('Предсказать'):
        if listing_type_text == "":
            st.write("Введите текст")
        else:
            data = {
                "features": [list]
            }

            url = "http://127.0.0.1:8000/predict"
            response = requests.post(url, json=data)
            result = response.json()
            price = result.get("predicted_price")
            st.write(f"Предсказанная цена: {price}")

    with tab2:
        tab2.subheader("Руководство пользователя")

        st.markdown(f"""
                    ### ⚠️ Для работы программы требуется запущенный API
                    """)