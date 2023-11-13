from datetime import datetime

import pandas as pd
import numpy as np

import plotly.graph_objects as go
import matplotlib.pyplot as plt

import streamlit as st
import requests

from modules.file.EfarDataFile import EfarDataFile

def client(df_application):
    def update(customers_references, customer_reference, base_url):
        predicted_proba = 0

        if customer_reference in customers_references:
            response = requests.get(f'{base_url}predict/{customer_reference}')

            if response:
                predicted_proba = float(response.json()['predicted_proba0'])
            else:
                print(f'\033[1m>>>\033[0m [{datetime.now()}][\033[1mCLIENT\033[0m] Le service API de scoring est introuvable {response}')
        
        score = predicted_proba * 100
        
        predicted_gauge = go.Figure(
            go.Indicator( 
                mode = 'gauge+number',
                value = score,
                domain = {
                    'x': [0, 1], 
                    'y': [0, 1]
                },
                gauge = {
                    'axis': {
                        'range': [0, 100], 
                        'tickwidth': 0.2, 
                        'tickcolor': 'darkblue'
                    },
                    'bgcolor': 'lightgreen',
                    'steps': [
                        {
                            'range': [0, 60], 
                            'color': 'red'
                        }
                    ],
                    'threshold': {
                        'line': {
                            'color': 'lightgreen', 
                            'width': 4
                        },
                        'thickness': 0.75,
                        'value': 100
                    }
                },
                title = {
                    'text': f'{"Prêt accepté".upper() if score > 60 else "Prêt refusé".upper()}'
                }
            )
        )
        return predicted_gauge

    def on_selectedchanged(selected):
        st.session_state['customer_reference'] = selected
        left_, center_, last_ = st.columns([0.23, 0.38, 0.38])

        with center_:
            fig = update(customers_references, selected, base_url)
            st.plotly_chart(fig)

        sex = df_application.loc[int(selected), 'CODE_GENDER']
        age = int(np.trunc(-int(df_application.loc[int(selected), 'DAYS_BIRTH']) / 365))
        family_status = df_application.loc[int(selected), 'NAME_FAMILY_STATUS']
        education_level = df_application.loc[int(selected), 'NAME_EDUCATION_TYPE']
        occupation_type = df_application.loc[int(selected), 'OCCUPATION_TYPE']
        own_realty = df_application.loc[int(selected), 'FLAG_OWN_REALTY']
        amount_income = str(df_application.loc[int(selected), 'AMT_INCOME_TOTAL'])
        contract_type = str(df_application.loc[int(selected), 'NAME_CONTRACT_TYPE'])
        amount_credit = str(df_application.loc[int(selected), 'AMT_CREDIT'])
        amount_annuity = df_application.loc[int(selected), 'AMT_ANNUITY'] / 12

        column1, column2, column3 = st.columns(3)

        with column1:
            st.header('Client')
            st.write(
                '_Sex_ : ',
                f'***{sex}***'
            )
            st.write(
                '_Age_ : ', 
                f'***{age}***'
            )
            st.write(
                '_Statut familial_ : ', 
                f'***{family_status}***'
            )
            st.write(
                '_Type de formation_ : ', 
                f'***{education_level}***'
            )
            st.write(
                '_Type de profession_ : ', 
                f'***{occupation_type}***'
            )
            st.write(
                '_Client propriétaire_ : ', 
                f'***{own_realty}***'
            )
            st.write(
                '_Revenu du client_ : ', 
                f'***{amount_income}***'
            )

        with column2:
            st.header('Contract')
            st.write(
                '_Type de contrat_ : ', 
                f'***{contract_type}***'
            )
            st.write(
                '_Montant du crédit_ : ', 
                f'***{amount_credit}***'
            )
            st.write(
                '_Mensualité du prêt_ : ',
                f'***{amount_annuity:.1f}***'
            )

        with column3:
            st.header('À Propos')
            st.write(
                """
                1. _Le prêt à dépenser est refusé pour un ***score*** inférieur à ***60***_
                2. _Le prêt à dépenser est accépté pour un ***score*** supérieur à ***60***_
                3. _Pour plus d'information, consulter la partie ***Analyse***_ 
                """
            )

    st.header('SCORING', divider='rainbow')
    st.subheader('_Modèle de scoring_ :blue[_Classification_] :sunglasses:')

    #base_url = 'http://127.0.0.1:5001/' 
    base_url = 'https://efar7-api-8b6b495cd473.herokuapp.com/'
    request_url = f'{base_url}customers/'
    response = requests.get(request_url)

    if response:
        customers_references = response.json()['customers_references']
        customers_references = list(np.sort(customers_references))
        selected = customers_references[0]
    else:
        customers_references = ['000000']
        print(f'\033[1m>>>\033[0m [{datetime.now()}][\033[1mCLIENT\033[0m] Le service API de scoring est introuvable {response}')

    with st.spinner('Wait for it...'):
        selected = st.selectbox(
            'Selectionner un client', 
            customers_references,
            #index=0 if 'customer_reference' not in st.session_state else customers_references.index(st.session_state.customer_reference),
            placeholder='Selectionner la reference du client...'
        )
        on_selectedchanged(selected)
        
        
