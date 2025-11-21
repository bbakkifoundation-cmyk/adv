import pandas as pd
import numpy as np
import joblib
import streamlit as st
model =joblib.load(open("linear_regression_model.joblib",'rb'))
st.title("sales prediction app")

TV=st.number_input("TV Adv Budget",min_value=0.0)
Radio=st.number_input("Radio Adv Budget",min_value=0.0)
Newspaper=st.number_input("Newspaper Budget",min_value=0.0)

if st.button('predict sales'):
	input_data=np.arrary([[TV,Radio,Newspaper]])
	prediction=model.predict(input_data)[0]
	st.success(f'predict sales:{prediction:.2f}')





