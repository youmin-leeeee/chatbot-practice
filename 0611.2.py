import streamlit as st
from langchain_community.chat_models import ChatOpenAI

st. set_page_config(page_title="Pregunta lo que quieres") #페이지 이름 설정
st.title("Pregunta lo que quieres, estoy aqui para ayudarte") #페이지 메인 텍스트 설정

import os
os. environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

def generate_response(input_text):
    llm = ChatOpenAI(temperature=0, model_name='gpt-4') #창의성 0
    st.info(llm.predict(input_text))
    #사용자가 입력한 질문을 llm에 입력하고 그 답을 페이지에 띄우겠다는 뜻

with st.form('Question'): #질문을 입력하는 칸을 페이지에 설정함
    text = st.text_area('Esscribe tu pregunta:',
                        "¿Qué tipo de modelos de texto proporciona OpenAI?")
    #질문을 입력하느누칸과ㅠ예시 질문 입력
    submitted = st.form_submit_button('ENVIARr') #질문 입력 후 버튼 활성화
    generate_response(text)
    #버튼이 눌리면 입력된 질문이 위에서 만든 generate_response에 input_text로 들어감
