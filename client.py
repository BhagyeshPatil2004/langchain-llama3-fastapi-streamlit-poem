# import requests
# import streamlit as st

# # def get_ollama_response(input_text):
# #     response=requests.post(
# #         "http://localhost:8000/poem/invoke",
# #         json={'input':{'topic':input_text}}
# #     )
# #     return response.json()['output']

# def get_ollama_response(input_text):
#     response = requests.post(
#         "http://localhost:8000/poem/invoke",
#         json={"input": {"topic": input_text}}
#     )
#     print(response.json())  # For debugging
#     return response.json()


# ## Streamlit framework

# st.title('Langchain Demo With LlaMa3 API')
# input_text=st.text_input("Write a poem on")

# if input_text:
#     st.write(get_ollama_response(input_text))

import requests
import streamlit as st

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/test",
        json={"topic": input_text}
    )
    data = response.json()
    if "output" in data:
        return data["output"]
    else:
        return f"Error: {data}"

## Streamlit framework

st.title('Langchain Demo With LlaMa3 API')
input_text = st.text_input("Write a poem on")

if input_text:
    st.write(get_ollama_response(input_text))
