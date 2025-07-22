
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama

from langchain_core.output_parsers import StrOutputParser


import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")



## prompt templates

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant, please response to user queies"),
        ("user","Question:{question}")
    ]
)

st.title('Langchain Demo With LLM API')
input_text=st.text_input("Search the topic u want")


options = ['Gemini', 'OpenAI', 'Ollma']
selected_models = st.multiselect("Select your Model:", options)

llm = None


for model in selected_models:
    if model == 'Gemini':
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
    elif model == 'OpenAI':
        llm=ChatOpenAI(model="gpt-3.5-turbo")
        pass
    elif model == 'Ollma':
        llm=Ollama(model="llama2")
        pass




    output_parser=StrOutputParser()
# OutputParser that parses LLMResult into the top likely string.
    chain= prompt | llm | output_parser


    if input_text:
        if st.button('submit'):
            st.write(chain.invoke({'question':input_text}))






