{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d899bf16-dd8e-4f15-afb2-12a21ad507aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "85979bf0-815d-410c-9779-36bf7742e036",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title('Loan Classification Predictive Model: \\n How much do you think incorrect Loan Approval costs the UK Banking sector annually?')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "102f4a0b-5682-4574-a03e-975eb47a2baa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.image('https://www.lendingtree.com/content/uploads/2020/01/mortgage-default-1140x524.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8098870-942c-478e-a4f7-1a25099b598b",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Textbox for user input\n",
    "number = st.number_input(\"How good is your predictive model. Enter the decimal percentage of false positives: (formula = (1 - specificity) Hint. Type in 0.999, that's the one from my best ML model ;)):\", min_value=0)\n",
    "\n",
    "error_rate = 1 - number\n",
    "baseline = 0.05\n",
    "# Calculation (example: square the number)\n",
    "cost = (int(0.35*200442*279606*error_rate))/1000000\n",
    "cost_baseline = (int(0.35*200442*279606*baseline))/1000000\n",
    "savings = (cost_baseline - cost)\n",
    "\n",
    "#create a dataframe\n",
    "models2 = {'Cost with predictive models' : cost, \n",
    "           'Cost without models': cost_baseline, \n",
    "               'Total annual saving': savings}\n",
    "    \n",
    "dct = {k:[v] for k,v in models2.items()}\n",
    "df_cost = pd.DataFrame(dct)\n",
    "\n",
    "if st.checkbox('Show savings comparison'):\n",
    "    st.bar_chart(df_cost, y_label = 'Money saved in £')\n",
    "\n",
    "# Show the result\n",
    "st.write(f'Cost with predictive models: {cost :.3f} million', f'Cost without models: {cost_baseline :.3f} million', f'The total saving to the UK Banking industry from incorrect Loan Classification is: {savings :.3f} million.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "86aba5ff-5339-4df6-b1e5-a05e611e0527",
   "metadata": {},
   "outputs": [],
   "source": [
    "if st.checkbox('Show savings comparison'):\n",
    "    st.bar_chart(df_cost, y_label = 'Money saved in £')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "268ad1d9-103f-4a62-ae57-a32c9abcabab",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
