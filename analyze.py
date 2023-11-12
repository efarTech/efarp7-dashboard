from datetime import datetime

import pandas as pd
import numpy as np

import plotly.graph_objects as go
import matplotlib.pyplot as plt

import streamlit as st
import shap

def analyze(
        df_api, 
        shap_explaine_expected_value, 
        shap_values, 
        shap_waterfall_expected_value,
        shap_values_waterfall
    ):
    def update(
            customer_reference, 
            df_api, 
            shap_explaine_expected_value, 
            shap_values, 
            shap_waterfall_expected_value,
            shap_values_waterfall
        ):
        df_customer = df_api.reset_index(drop=False)
        customer_index = df_customer[df_customer['SK_ID_CURR'] == int(customer_reference)]
        customer_index = customer_index.index.values[0]
        
        if isinstance(shap_explaine_expected_value, list):
            if len(shap_explaine_expected_value) > 1:
                shap_explaine_expected_value = shap_explaine_expected_value[1]
            else:
                shap_explaine_expected_value = shap_explaine_expected_value[0]

        if isinstance(shap_waterfall_expected_value, list):
            if len(shap_waterfall_expected_value) > 1:
                shap_waterfall_expected_value = shap_waterfall_expected_value[1]
            else:
                shap_waterfall_expected_value = shap_waterfall_expected_value[0]
        
        fig_waterfall_plot = shap.plots._waterfall.waterfall_legacy(
            shap_waterfall_expected_value, 
            shap_values_waterfall[customer_index].values[:, 0], 
            feature_names=df_api.columns, 
            max_display=20, 
            show=False
        )
        fig_force_plot = shap.force_plot(
            shap_explaine_expected_value, 
            shap_values[0][customer_index], 
            df_api.iloc[customer_index],
            matplotlib=True, 
            show=False
        )
        return fig_force_plot, fig_waterfall_plot
    
    st.header('ANALYSE', divider='rainbow')
    st.subheader('_Modèle de scoring_ :blue[_Classification_] :sunglasses:')
    
    if 'customer_reference' in st.session_state:
        customer_reference = int(st.session_state.customer_reference)
        st.write(
            f"""
            **Réference du client**
            
                {customer_reference}
            """
        )
        fig_force_plot, fig_waterfall_plot = update(
            customer_reference, 
            df_api, 
            shap_explaine_expected_value, 
            shap_values, 
            shap_waterfall_expected_value,
            shap_values_waterfall
        )
        st.write(
            """
            **Visualisation de l'influence des caractérisques**
            """
        )
        fig, ax = plt.subplots(nrows=1, ncols=1)
        fig = fig_waterfall_plot
        st.pyplot(fig)
        
        st.write(
            """
            **Visualisation de la contribution des caractéristiques**
            """
        )
        fig, ax = plt.subplots(nrows=1, ncols=1)
        fig = fig_force_plot
        st.pyplot(fig)
    else:
        st.error('Un client doir être sélectionné!')
    
