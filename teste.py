import streamlit as st
import requests

st.set_page_config(page_title="Piadas Aleatórias", page_icon="😂")

st.title("😂 Navegador de Piadas Aleatórias")
st.markdown("Clique abaixo para uma piada aleatória!")

# Selecionar tipo de piada
piada_tipo = st.radio("Escolha o tipo de piada:", ["Chuck Norris", "Piada de Pai"])

# Função para pegar piada de Chuck Norris
def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    return data['value']

# Função para pegar piada de Pai
def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['joke']

# Mostrar piada aleatória com base na escolha
if piada_tipo == "Chuck Norris":
    if st.button("Gerar Piada de Chuck Norris"):
        piada = get_chuck_norris_joke()
        st.subheader("Piada do Chuck Norris")
        st.write(piada)
else:
    if st.button("Gerar Piada de Pai"):
        piada = get_dad_joke()
        st.subheader("Piada de Pai")
        st.write(piada)
