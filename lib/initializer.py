import streamlit as st


def Initializer():
    st.markdown("""
        # Arthurtuio web page #

        Bem vindo ao meu espaço na internet!!
    """)

    st.image(
        image='images/welcome.jpg',
        width=350
    )

    st.markdown("""    
        **Aqui você vai poder conhecer um pouco mais sobre mim, meus projetos, 
        e minhas experiências profissionais!**

        Pra navegar por esses tópicos, basta acessar o painel no canto esquerdo superior,
        e selecionar a opção que deseja saber mais, conforme esse gif aqui :)

        Já adianto que se caso você trocar alguma ideia, dar algum feedback, 
        tirar alguma dúvida, basta me adicionar em algumas das minhas redes sociais!! 
    """)

    # imagem = st.image("Adicionar um gif maroto aqui explicando como acessar")