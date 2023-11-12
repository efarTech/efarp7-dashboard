from datetime import datetime

import streamlit as st
import base64
import yaml
import streamlit_authenticator as authenticator

from yaml.loader import SafeLoader

def run(config_file):    
    login_header_placeholder = st.header('LOGIN', divider='rainbow')
    login_subheader_placeholder = st.subheader('_Accès contrôlé_ :blue[_Authentification_] :sunglasses:')

    with open(config_file) as file:
        config = yaml.load(file, Loader=SafeLoader)

        authenticate = authenticator.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days'],
            config['preauthorized']
        )
        authenticate.login('Login', 'main')

    return authenticate, login_header_placeholder, login_subheader_placeholder
