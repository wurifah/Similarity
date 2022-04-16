#import package
import streamlit as st
import pandas as pd
import numpy as np

from difflib import SequenceMatcher

#import the data
data = pd.read_csv(r"C:\tutorial python\similarity\Precily_Text_Similarity.csv")
print(data)

st.title("Similarity Text Checker")


#input the texts
text1 = st.slider("Input the first text",str(data.text1))
text2 = st.slider("Input the second text",str(data.text2))

def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()

similarity = similar(text1, text2)

#checking similarity ratio
if st.button("Check the similarity rate"):
    st.header("The similarity rate of those texts is {}".format(int(similarity)))