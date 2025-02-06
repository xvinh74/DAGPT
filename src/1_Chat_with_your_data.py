import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

from src.logger.base import BaseLogger
from src.models.llms import load_llm

# Load enviroment variables
load_dotenv()
logger = BaseLogger()

MODEL_NAME = "gpt-3.5-turbo"

def main():
    # 1. setup streamlit interface
    st.set_page_config(
        page_title="Smart Data Analysis Tool",
        page_icon=":bar_chart:",
        layout="centered"
    )
    
    # 2. load llms model
    llm = load_llm(model_name = MODEL_NAME)
    logger.info(f"### Successfully load {MODEL_NAME} !###")
    
    
    # 3. upload csv file
    
    
    # 4. initial chat history
    
    
    
    # 5. read csv file
    
    
    
    # 6. create data analysis agent
    
    
    
    # 7. input query and process query
    
    
    
    
    # 8. display chat history
    
    
    
    


if __name__ == "__main__":
    main()

