import streamlit as st


def MyExperiences():
    st.markdown("""
        ## **2. Sobre minhas experiências profissionais e de vida** ##

        Aqui eu compilo as experiências profissionais que já tive,
        e também compartilho algumas experiências de vida, sejam na área
        da programação ou não :)
        
        Pra navegar pelas experiências, basta selecionar na opção abaixo:
            
    """)

    experiencias_list = [
        "Profissional | Engenheiro de Dados na Conta Azul",
        "Pessoal | Facilitador de tutorial na Python Brasil 2020",
        "Pessoal | Um breve relato dos meus 4 anos na AIESEC",
        "Pessoal | Meu intercâmbio voluntário na Colômbia em 2017",
        # No futuro vem mais experiências
    ]

    experiencia_selecionada = st.selectbox(
        "Selecione o experiencia que deseja saber mais",
        experiencias_list
    )

    st.markdown("""
        _______________________
    """)
