import streamlit as st

def home():    
    st.header('Prêt à dépenser', divider='rainbow')
    st.subheader('_Crédits à la consommation_ :blue[_Scoring crédit_] :sunglasses:')
    st.empty()
    
    _, center_column, _ = st.columns(3)
    center_column.image('./repositories/data/pretadepenser.png', width=300)
    
    st.write(
        """
        **Client**
        
            Information et type de contrat pour le crédit souscrit par client avec le score prédit
                
        **Analyse**
        
            Visualisation des caractérisques qui influencent ou contrinuent sur la prédiction du score
        """
    )
