import streamlit as st
import numpy as np
import pandas as pd
import pickle
model=pickle.load(open('finalized_model_RF.pkl','rb'))


def comp_st(cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age):
    input=np.array([[cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age],])
    prediction=model.predict(input)
    return float(prediction)

def main():
    st.title("Concrete compressive strength prediction")
    st.image("cube.jpg")
    st.header("Tired of crushing the cubes and waiting for 28 days just to know the concrete strength??")
    st.header("Then let's put our machine learning model to some good use.")
    st.markdown("Herein i have created a machine learning model which takes the values of ingredients as input and predict the compressive strength in no time. Quite interesting huh??")
    st.markdown("lets check...")

    cement = st.number_input("cement in kg",format="%.1f")
    blast_furnace_slag = st.number_input("blast_furnace_slag in kg",format="%.1f")
    fly_ash = st.number_input("fly_ash in kg",format="%.1f")
    water = st.number_input("water in kg",format="%.1f")
    superplasticizer = st.number_input("superplasticizer in kg",format="%.1f")
    coarse_aggregate = st.number_input("coarse_aggregate in kg",format="%.1f")
    fine_aggregate = st.number_input("fine_aggregate in kg",format="%.1f")
    age = st.number_input("age in days",step=1)


    if st.button("predict the strength of your mix design "):
        output = comp_st(cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age)
        st.success("The compressive strength of the above combination is most probably {} MPa".format(output))

        if output > 40:
            st.write("concrete is having high strength.")
        elif output <=40 and output >20:
            st.write("concrete is having moderate strength.")
        else:
            st.write("concrete is having low strength.")

if __name__=='__main__':
    main()
