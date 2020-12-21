import streamlit as st


def MyProjects():
    st.markdown("""
        ## **1. Sobre meus projetos** ##

        Desde que engressei no mundo da programação, tive a oportunidade
        de tirar algumas ideias da gaveta e transformá-las em projetos.
    
        Pra navegar pelos projetos, basta selecionar na opção abaixo:
    """)

    projetos_list = [
        "Leitor de fatura de conta de luz - TCC",
        "O de Magic",
        # No futuro vem mais projetos
    ]

    projeto_selecionado = st.selectbox(
        "Selecione o projeto que deseja saber mais",
        projetos_list
    )

    st.markdown("""
        _______________________
    """)

    if projeto_selecionado == projetos_list[0]:
        st.markdown("Under construction ...")