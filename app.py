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
    
    Month = st.selectbox("Select the Month", ("January", "February", "March", "April", "May", "June", "July",
                                              "August", "September", "October", "November", "December"))
    if Month == "January":
        Month = 1
    elif Month == "February":
        Month = 2
    elif Month == "March":
        Month = 3
    elif Month == "April":
        Month = 4
    elif Month == "May":
        Month = 5
    elif Month == "June":
        Month = 6
    elif Month == "July":
        Month = 7
    elif Month == "August":
        Month = 8
    elif Month == "September":
        Month = 9
    elif Month == "October":
        Month = 10
    elif Month == "November":
        Month = 11    
    else:
        Month = 12    
    
    Airline = st.selectbox("Flight airline", ('05U', '3J', '3W', '5H', 'AT1', 'AT', 'B5', 'BA', 'CZ', 'D3', 'DO',
       'EK', 'EY', 'F8', 'G9', 'KL', 'LH', 'LX', 'MK', 'MS', 'PW', 'QR',
       'SA', 'SV', 'TK', 'TM', 'WB', 'WY', 'XU', '03R', 'ET', 'JM', 'KQ',
       'UNS'))
    if Airline == "05U":
        Airline = 1
    elif Airline == "3J":
        Airline = 2
    elif Airline == "3W":
        Airline = 3
    elif Airline == "5H":
        Airline = 4
    elif Airline == "AT1":
        Airline = 5
    elif Airline == "AT":
        Airline = 6
    elif Airline == "B5":
        Airline = 7
    elif Airline == "BA":
        Airline = 8
    elif Airline == "CZ":
        Airline = 9
    elif Airline == "D3":
        Airline = 10
    elif Airline == "DO":
        Airline = 11
    elif Airline == "EK":
        Airline = 12
    elif Airline == "EY":
        Airline = 13
    elif Airline == "F8":
        Airline = 14
    elif Airline == "G9":
        Airline = 15
    elif Airline == "KL":
        Airline = 16
    elif Airline == "LH":
        Airline = 17
    elif Airline == "LX":
        Airline = 18
    elif Airline == "MK":
        Airline = 19
    elif Airline == "MS":
        Airline = 20
    elif Airline == "PW":
        Airline = 21
    elif Airline == "QR":
        Airline = 22
    elif Airline == "SA":
        Airline = 23
    elif Airline == "SV":
        Airline = 24
    elif Airline == "TK":
        Airline = 25
    elif Airline == "TM":
        Airline = 26
    elif Airline == "WB":
        Airline = 27
    elif Airline == "WY":
        Airline = 28
    elif Airline == "XU":
        Airline = 29
    elif Airline == "03R":
        Airline = 30
    elif Airline == "ET":
        Airline = 31
    elif Airline == "JM":
        Airline = 32
    else:
        Airline = 33
   
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
            [Day, Month, Airline, flightclass, capacity, season])

    st.success(prediction_analysis)


if __name__ == '__main__':
    main()
