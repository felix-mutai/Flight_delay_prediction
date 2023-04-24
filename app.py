import numpy as np
import pickle
import streamlit as st
from threading import local
import pandas as pd



# loading the saved model
loaded_model = pickle.load(open('model.pkl', 'rb'))


# creating a function for Prediction

def flight_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The flight will not delayed'
    else:
        return 'The flight will delay'


def main():
    # giving a title
    st.title('The Flight Prediction Web App')

    # getting the input data from the user

    Day = st.text_input('Date of the Month')
    Month = st.text_input('The month')
    Airline = st.text_input('Flight airline')

    flightclass = st.selectbox("Flight Class (International/Domestic)", ("INT", "DOM"))
    if flightclass == "INT":
        flightclass = 1
    else:
        flightclass = 0

    capacity = st.text_input('Flight Capacity')    
    season = st.selectbox("Season", ("Summer", "Winter"))
    if season == "Summer":
        season = 1
    else:
        season = 0

    # code for Prediction
    prediction_analysis = ''

    # creating a button for Prediction

    if st.button('Flight prediction results'):
        prediction_analysis = flight_prediction(
            [Day, Month, Airline, flightclass, capacity,timediff,night1, season])

    st.success(prediction_analysis)


if __name__ == '__main__':
    main()
