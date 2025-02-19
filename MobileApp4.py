import streamlit as st
import pandas as pd
import numpy as np

st.title('Loan Classification Predictive Model: \n How much do you think incorrect Loan Approval costs the UK Banking sector annually?')

st.image('https://www.lendingtree.com/content/uploads/2020/01/mortgage-default-1140x524.jpg')


# Textbox for user input
number = st.number_input("How good is your predictive model. Enter the decimal percentage of false positives: (formula = (1 - specificity) Hint. Type in 0.999, that's the one from my best ML model ;)):", min_value=0)

error_rate = 1 - number
baseline = 0.05
# Calculation (example: square the number)
cost = (int(0.35*200442*279606*error_rate))/1000000
cost_baseline = (int(0.35*200442*279606*baseline))/1000000
savings = (cost_baseline - cost)

#create a dataframe
models2 = {'Cost with predictive models' : cost, 
           'Cost without models': cost_baseline, 
               'Total annual saving': savings}

# Show the result
st.write(f'Cost with predictive models: {cost :.3f} million', f'Cost without models: {cost_baseline :.3f} million', f'The total saving to the UK Banking industry from incorrect Loan Classification is: {savings :.3f} million.')

