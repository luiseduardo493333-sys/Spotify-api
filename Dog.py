import streamlit as st
import requests

st.set_page_config(page_title="Raças de Cachorros", page_icon="🐶")

st.title("🐶 Navegador de Raças de Cachorros")
st.markdown("Explore diferentes raças e veja fotos fofas!")


@st.cache_data
def get_dog_breeds():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    data = response.json()
    return data['message']

breeds_data = get_dog_breeds()

breed_options = []

for breed, sub_breeds in breeds_data.items():
    if sub_breeds:
        for sub in sub_breeds:
            breed_options.append(f"{breed} - {sub}")
    else:
        breed_options.append(breed)

breed_options.sort()

selected = st.selectbox("Escolha uma raça:", breed_options)

if " - " in selected:
    breed, sub_breed = selected.split(" - ")
    image_url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random"
else:
    breed = selected
    image_url = f"https://dog.ceo/api/breed/{breed}/images/random"

def get_dog_image(url):
    response = requests.get(url)
    data = response.json()
    return data['message']

img = get_dog_image(image_url)

st.image(img, caption=f"{selected.capitalize()}", use_column_width=True)
