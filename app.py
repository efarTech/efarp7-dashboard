import streamlit as st
import login, home, client, analyze
import logging

from repositories.EfarRepository import EfarRepository
from controllers.EfarScoringController import EfarScoringController
from controllers.EfarLoginController import EfarLoginController
from controllers.EfarShapController import EfarShapController

logging.getLogger().disabled = True

def main(
        df_api, 
        df_application, 
        shap_explaine_expected_value, 
        shap_values, 
        shap_waterfall_expected_value,
        shap_values_waterfall
    ):
    st.sidebar.write('# Prêt à dépenser')
    st.sidebar.write('## Welcome ', f'*{st.session_state["name"]}*')
    options = st.sidebar.radio(
        'Select view',
        [
            'Home', 
            'Client', 
            'Analyse'
        ]
    )
    if options == 'Home':
        home.home()
    elif options == 'Client':
        client.client(df_application)
    elif options == 'Analyse':
        analyze.analyze(
            df_api, 
            shap_explaine_expected_value, 
            shap_values, 
            shap_waterfall_expected_value,
            shap_values_waterfall
        )

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide", page_title='dashboard')

repository = EfarRepository('./repositories/data/')
scoringController = EfarScoringController(repository)
loginController = EfarLoginController(repository)
shapController = EfarShapController(repository)

authenticate, login_header_placeholder, login_subheader_placeholder = login.run('./config.yaml')

if st.session_state["authentication_status"]:
    column1, column2 = st.columns([1, 0.08])

    with column2:
        authenticate.logout('Logout', 'main', key='efar-scoring')
    
    login_header_placeholder.empty()
    login_subheader_placeholder.empty()

    main(
        scoringController.get_api(), 
        scoringController.get_application(), 
        shapController.get_shap_explaine_expected_value(), 
        shapController.get_shap_values(), 
        shapController.get_shap_waterfall_expected_value(),
        shapController.get_shap_values_waterfall()
    )
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

