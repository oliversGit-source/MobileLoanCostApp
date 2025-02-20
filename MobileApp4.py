import streamlit as st
import pandas as pd
import numpy as np

st.title('Loan Classification Predictive Model: \n How much do you think incorrect Loan Approval costs the UK Banking sector annually?')

st.image('https://www.lendingtree.com/content/uploads/2020/01/mortgage-default-1140x524.jpg')

st.write("Precision Specificity measures the proportion of actual negative instances that were correctly identified by the classifier.  \nIt provides insight into the classifier’s ability to avoid false positives.  \nThe best performing predictive model in this study had a specificity of 0.999.")

# Textbox for user input
number = st.number_input("How good is your predictive model? Enter the specificity of your model below, and then click the 'Calculate' button.")

st.write("The specificity of your predicted model is:", number)

error_rate = (1 - number)
baseline = 0.05
# Calculation (example: square the number)
factor = (0.35*200442*279606)/1000000
cost_in_mill = factor*error_rate
cost_baseline_in_mill = factor*baseline
savings = (cost_baseline_in_mill - cost_in_mill)


models2 = {'Cost with predictive models' : cost_in_mill, 
           'Cost without models': cost_baseline_in_mill, 
           'Total annual saving': savings}

if(st.button('Calculate')):
# Show the result
           st.write(f'Cost with predictive models: {cost_in_mill :.3f} million', f'Cost without models: {cost_baseline_in_mill :.3f} million', f'The total saving to the UK Banking industry from incorrect Loan Classification is: {savings :.3f} million.')

# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("This is an online mobile app created by Oliver Butterworth-Bakhshi for an Imperial Business School Data Analytics Project.")
