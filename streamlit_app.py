import streamlit as st
import pandas as pd
import os

# Загрузка файла
def save_uploaded_file(uploaded_file):
    with open(os.path.join("./", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Загрузка MP3 файла",
        page_icon="🎵",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Custom CSS for background image
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://example.com/background_image.jpg');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Конспектор ^_^")

    uploaded_file = st.file_uploader("Выберите MP3 файл", type=["mp3"])

    if uploaded_file is not None:
        save_uploaded_file(uploaded_file)
        st.success("Файл успешно загружен!")

if __name__ == "__main__":
    main()
# Выбор языка вывода
language = st.selectbox(
   'Выберите язык вывода',
   ('Русский', 'Английский', 'Французский')
)

# Кнопка "Пуск"
if st.button('Пуск'):
   # Здесь вы можете добавить код для обработки данных в выбранном языке
   st.write('Обработка данных...')

# Кнопка для скачивания результата
if st.button('Скачать результат'):
   # Здесь вы можете добавить код для генерации и скачивания файла
   st.write('Генерация файла...')
