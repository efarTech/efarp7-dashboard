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
        decidion = f'{"Prêt accepté".upper() if score > 60 else "Prêt refusé".upper()}'
        
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
                    'text': decidion
                }
            )
        )
        return predicted_gauge, decidion

    def on_selectedchanged(df_application, customers_references, base_url, selected):
        st.session_state['customer_reference'] = selected
        left_, center_, last_ = st.columns([0.23, 0.38, 0.38])

        with center_:
            fig, decidion = update(customers_references, selected, base_url)
            st.plotly_chart(fig)

        column1, column2, column3, column4 = st.columns(4)

        with column1:
            st.header('CLIENT')
            st.write(
                '_Sex_ : ',
                f'***{df_application.loc[int(selected), "CODE_GENDER"]}***'
            )
            st.write(
                '_Age_ : ', 
                f'***{":green[" if "Prêt accepté".upper() == decidion else ":red[" }{int(np.trunc(-int(df_application.loc[int(selected), "DAYS_BIRTH"]) / 365))}]***'
            )
            st.write(
                '_Statut familial_ : ', 
                f'***{df_application.loc[int(selected), "NAME_FAMILY_STATUS"]}***'
            )
            st.write(
                '_Type de formation_ : ', 
                f'***{df_application.loc[int(selected), "NAME_EDUCATION_TYPE"]}***'
            )
            st.write(
                '_Type de profession_ : ', 
                f'***{df_application.loc[int(selected), "OCCUPATION_TYPE"]}***'
            )
            st.write(
                '_Client propriétaire_ : ', 
                f'***{df_application.loc[int(selected), "FLAG_OWN_REALTY"]}***'
            )
            st.write(
                '_Revenu du client_ : ', 
                f'***{":green[" if "Prêt accepté".upper() == decidion else ":red[" }{str(df_application.loc[int(selected), "AMT_INCOME_TOTAL"])}]***'
            )

        with column2:
            st.header('CONTRAT')
            st.write(
                '_Type de contrat_ : ', 
                f'***{str(df_application.loc[int(selected), "NAME_CONTRACT_TYPE"])}***'
            )
            st.write(
                '_Montant du crédit_ : ', 
                f'***{":green[" if "Prêt accepté".upper() == decidion else ":red[" }{str(df_application.loc[int(selected), "AMT_CREDIT"])}]***'
            )
            st.write(
                '_Mensualité du prêt_ : ',
                f'***{":green[" if "Prêt accepté".upper() == decidion else ":red[" }{df_application.loc[int(selected), "AMT_ANNUITY"] / 12:.1f}]***'
            )

        with column3:
            st.header('MOYENNE')
            st.dataframe(
                df_application[['DAYS_BIRTH', 'AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY']].assign(
                    DAYS_BIRTH=np.trunc(-df_application.DAYS_BIRTH / 365),
                    AMT_ANNUITY=df_application['AMT_ANNUITY'] / 12
                ).rename(
                    columns={
                        'DAYS_BIRTH': 'Age du client', 
                        'AMT_INCOME_TOTAL': 'Revenu du client',
                        'AMT_CREDIT': 'Montant du crédit',
                        'AMT_ANNUITY': 'Mensualité du prêt',
                    }
                ).mean().to_frame(name='Les moyennes')
            )
        
        with column4:   
            st.header('INFORMATION')
            st.write(
                """
                1. _Prêt à dépenser est refusé: :red[***Score*** < ***60***]_
                2. _Prêt à dépenser est accépté: :green[***Score*** > ***60***]_
                3. _Décision: voir la partie ***Analyse***_ 
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
            placeholder='Selectionner la reference du client...'
        )
        on_selectedchanged(df_application, customers_references, base_url, selected)
        
        
