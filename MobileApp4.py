import streamlit as st
import pandas as pd
import numpy as np

st.title('Loan Classification Predictive Model: \n How much do you think incorrect Loan Approval costs the UK Banking sector annually?')

st.image('https://www.lendingtree.com/content/uploads/2020/01/mortgage-default-1140x524.jpg')

st.text("Precision Specificity measures the proportion of actual negative instances that were correctly identified by the classifier. It complements recall by focusing on the negative class, providing insight into the classifier’s ability to avoid false positives.
Specificity, also known as the True Negative Rate (TNR), measures the proportion of actual negative instances that are correctly identified as negative by a model. It reflects how well the model avoids false positives.
Specificity = 𝑇𝑁/𝑇𝑁+𝐹𝑃")

# Textbox for user input
number = st.number_input("How good is your predictive model? Enter the specificity of your model:", min_value=0)


if(st.button('Calculate')):
# Show the result
           
           error_rate = 1 - number
           baseline = 0.05
           # Calculation (example: square the number)
           cost = int(0.35*200442*279606*error_rate)/1000000
           cost_baseline = int(0.35*200442*279606*0.05)/1000000
           savings = (cost_baseline - cost)


           models2 = {'Cost with predictive models' : cost, 
                      'Cost without models': cost_baseline, 
                          'Total annual saving': savings}
           
           st.write(f'Cost with predictive models: {cost :.3f} million', f'Cost without models: {cost_baseline :.3f} million', f'The total saving to the UK Banking industry from incorrect Loan Classification is: {savings :.3f} million.')

# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("This is an online mobile app created by Oliver Butterworth-Bakhshi for an Imperial Business School Data Analytics Project.")
