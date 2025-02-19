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
   "execution_count": 22,
   "id": "27513196-e713-45a6-8f30-55b40917728c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter specificity of predictive model as a percentage. 0.999\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "('Cost with predictive models: 19.616 million',\n",
       " 'Cost without models: 980.784 million',\n",
       " 'The total saving to the UK Banking industry from incorrect Loan Classification is: 961.168 million.')"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#create a model to estimate costs\n",
    "\n",
    "#average size of loan offered by a UK Building Society\n",
    "#The average size of a mortgage taken out in the Q4 of 2024 was £200,442.\n",
    "    \n",
    "#Source: https://www.finder.com/uk/mortgages/mortgage-statistics\n",
    "#Analysis conducted by finder.com\n",
    "\n",
    "#total number of mortgages approved in UK in Q1 of 2024:\n",
    "#279,606\n",
    "#https://www.uswitch.com/mortgages/mortgage-statistics/\n",
    "\n",
    "#average annual default rate on secure loans/mortgage is 5%, 0.05.\n",
    "#https://www.mortgagestrategy.co.uk/news/lenders-report-rising-mortgage-defaults-boe/\n",
    "\n",
    "def LoanCost():\n",
    "    #error rate is 1-specificity, i.e. percentage that were false positives\n",
    "    error_rate = (1 - float(input(\"Enter specificity of predictive model as a percentage.\")))\n",
    "    #use average annual default rate as a baseline: \n",
    "    baseline = 0.05\n",
    "    #average cost of each false positive - a loan approved on which a customer defaults on their payments\n",
    "    # this is typically 20%-50% of the total loan amount\n",
    "    # FORMULA: cost = cost of fp * average size of mortgage * number of mortagages approved * percentage of fp / (in millions)\n",
    "    cost = (int(0.35*200442*279606*error_rate))/1000000\n",
    "    cost_baseline = (int(0.35*200442*279606*baseline))/1000000\n",
    "    savings = (cost_baseline - cost)\n",
    "\n",
    "    models2 = {'Cost with predictive models' : cost, \n",
    "           'Cost without models': cost_baseline, \n",
    "               'Total annual saving': savings}\n",
    "    \n",
    "    dct = {k:[v] for k,v in models2.items()}\n",
    "    df_cost = pd.DataFrame(dct)\n",
    "    return f'Cost with predictive models: {cost :.3f} million', f'Cost without models: {cost_baseline :.3f} million', f'The total saving to the UK Banking industry from incorrect Loan Classification is: {savings :.3f} million.'\n",
    "\n",
    "LoanCost()\n",
    "\n",
    "\n"
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
