import streamlit as st


from lib.initializer import Initializer
from lib.my_contacts import MyContact


class MainPage:
    def __init__(self): pass

    def initialize(self):

        topicos_list = [
            "0. Página inicial",
            "1. Meus projetos <3",
            "2. Experiências profissionais e de vida",
            "3. Meus contatos",
        ]

        topico_selecionado = st.sidebar.selectbox(
            "Lalala",
            topicos_list,
        )

        if topico_selecionado == topicos_list[0]:
            Initializer()

        elif topico_selecionado == topicos_list[1]:
            st.write("Under Construction...")

        elif topico_selecionado == topicos_list[2]:
            st.write("Under Construction...")

        elif topico_selecionado == topicos_list[3]:
            MyContact()
#
#         elif topico_selecionado == topicos_list[2]:
#             self._subscribe_python_br_2020()
#
#         elif topico_selecionado == topicos_list[3]:
#             self._example_app()
#
#         elif topico_selecionado == "5.Sobre mim e meu contato":
#             self._my_contact()
#
#         elif topico_selecionado == "6.Tutoriais das tecnologias":
#             ToolsTutorial()
#
#     def _descriptions(self):
#         st.markdown("""
#             ## **1. Tecnologias Utilizadas Neste Tutorial** ##
#
#             Para entender mais sobre as tecnologias, basta fazer a seleção abaixo:
#         """)
#
#         resultado = st.selectbox(
#             "Qual tecnologia você quer conhecer?",
#             ("Streamlit", "Heroku", "Git")
#         )
#
#         if resultado == "Streamlit":
#             self._streamlit_description()
#
#         elif resultado == "Heroku":
#             self._heroku_description()
#
#         elif resultado == "Git":
#             self._git_description()
#
#     @staticmethod
#     def _config_local_environment():
#         st.markdown("""
#             ## **2. Configurando o ambiente local** ##
#
#             Pra você conseguir rodar o conteúdo dessa aplicação, e criar o conteúdo que quiser usando
#             estas ferramentas, existem alguns pré-requisitos que você precisa ter. São eles:
#
#                 1. Conhecimento básico sobre Python - e também alguma familiaridade com estruturas de dados.
#                 2. Ter alguma ferramenta (IDE) que permita programar em Python em seu PC.
#
#             Sobre IDE, recomendo PyCharm Community (CE) ou Visual Studio Code, no caso do Windows.
#             - Para fazer o download do Pycharm CE: https://www.jetbrains.com/pt-br/pycharm/download/
#             - Para fazer o download do VSCode: https://code.visualstudio.com/download
#
#             Além dessas, se você já entender de Github, vai ver que será muito fácil preparar sua aplicação.
#             **Se você não entende, se inscreve aí na Python Brasil 2020 e vai no meu tutorial!**
#             Ou, se a conferência já passou, tá tranquilo, você só vai precisar criar uma conta no **Github**,
#             e saber realizar `Fork`, e usar o comando `git clone`.
#
#             Criei um tutorial pra ajudar nessa parte do Github, para acessar, só ir para o item 6.1 :)
#
#             Ou, se preferir checar a documentação do github:
#             > - Pra criar conta é só acessar aqui: https://github.com/join
#             > - Esse site aqui explica como usar `git clone`:
#             https://docs.github.com/pt/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository
#
#             O link pra inscrição da conferência está no bloco `3. Inscrição para a Python Brasil 2020`
#         """)
#
#     @staticmethod
#     def _subscribe_python_br_2020():
#         st.markdown("""
#             ## **3. Inscrição para a Python Brasil 2020** ##
#
#             Sobre a conferência:
#
#             *A Python Brasil 2020 é a maior conferência sobre linguagem de programação Python do Brasil e da América Latina.*
#
#             *Feita pela comunidade para a comunidade, tem o objetivo de difundir a linguagem, disseminar conhecimento,
#             promover a troca de experiências e manter a comunidade crescendo igualmente em público e impacto social.*
#
#             *Este ano, em caráter de exceção devido à pandemia de covid-19, a Python Brasil será realizada remotamente,
#             organizada por um time distribuído no Brasil e no mundo, a fim de prosseguir com o seu objetivo
#             de disseminar conhecimento e aproximar pessoas.*
#
#             *Serão sete dias de imersão, onde participantes poderão contribuir para projetos de software livre,
#             participar de treinamentos e adquirir novos conhecimentos com outras pessoas da comunidade.*
#
#             Para se inscrever basta acessar esse site: https://2020.pythonbrasil.org.br/
#             Para ver a programação, aqui: https://2020.pythonbrasil.org.br/grade/
#
#             Você também pode acompanhar as palestras no canal da Python Brasil do Youtube, tanto
#             ao vivo quanto ou a hora que desejar! https://www.youtube.com/c/pythonbrasiloficial
#
#             **Esse tutorial será dado no domingo, dia 08, das 14h às 17h!**
#         """)
#
#     def _example_app(self):
#         st.markdown("""
#             ## **4. Um pouco do que você pode fazer com essa ferramenta** ##
#
#             Pra dar aquele gostinho do potencial da ferramenta, só clicar nas `checkboxes`
#             abaixo e ver algumas coisas do que é possível fazer :)
#         """)
#
#         st.image("https://media.giphy.com/media/ule4vhcY1xEKQ/giphy.gif")
#
#         if st.checkbox("Analisar tabelas/dataframes e gerar gráficos dos mesmos!"):
#             st.markdown("""
#                 #### **Analisar tabelas/dataframes e gerar gráficos dos mesmos!** ####
#
#                 **Além de analisar, podemos também influenciar na criação, ou filtrar a tabela direto por aqui!**
#
#                 Como exemplo, crie uma tabela com dados aleatórios, com os dados podendo ser de 0 até um valor
#                 que você define!
#             """)
#             limite_superior = st.slider(
#                 "Qual o valor máximo que você quer os dados aletórios?",
#                 min_value=1, max_value=100, value=1
#             )
#
#             numero_colunas = st.slider(
#                 "Quantas colunas você quer que essa tabela tenha?",
#                 min_value=2, max_value=5, value=2
#             )
#
#             nomes_colunas = self._create_column_names(numero_colunas)
#
#             chart_data = pd.DataFrame(
#                 np.random.randint(
#                     0, limite_superior, size=(100, numero_colunas)
#                 ),
#                 columns=nomes_colunas
#             )
#
#             st.write("Resultado:")
#             st.dataframe(chart_data)
#
#             st.write("Vamos gerar um gráfico disso!")
#             plot_type = st.selectbox(
#                 "Qual tipo de gráfico você quer?",
#                 ("bar_chart", "area_chart", "line_chart")
#             )
#
#             self._make_plot(plot_type, chart_data)
#
#         if st.checkbox("Essa página!"):
#             st.markdown("""
#                 #### **Essa página!** ####
#
#                 Essa página foi criada através de um código em **Python**, usando o framework **Streamlit**
#                 (que na prática é uma biblioteca para o Python), e o código da mesma pode ser visto aqui:
#                 https://github.com/arthurtuio/streamlit-heroku-python-br2020/blob/master/tutorial_introduction.py
#
#                 Se você curtiu, e quer aprender mais sobre, só dar uma conferida no repositório do **github**
#                 que tem esse código! E já deixo também o convite pra participares do tutorial que facilitarei
#                 na Python Brasil 2020, onde vou explicar tudo que tem lá e mais coisas!!
#             """)
#

#
#     @staticmethod
#     def _streamlit_description():
#         st.markdown("""
#             ### **Streamlit** ###
#
#             De acordo com eles, é a *maneira mais rápida de criar e compartilhar aplicações de dados.*
#
#             A documentação deles é ótima, tornando bem tranquilo o aprendizado da ferramenta por conta própria.
#
#             Para conferir, só acessar o site: https://www.streamlit.io/
#
#             Essa página web foi criada usando `streamlit`!
#         """)
#
#     @staticmethod
#     def _heroku_description():
#         st.markdown("""
#             ### **Heroku** ###
#
#             É uma plataforma de nuvem como serviço (Cloud Platform as a Service - PaaS).
#
#             Suporta diversas linguagens de programação.
#
#             Permite a criação, execução e operação de aplicações, tudo de forma
#             bem simples, tirando aquele stress de mexer com infraestrutura.
#
#             Pra saber mais sobre, só acessar o site: https://www.heroku.com/what#
#
#             Essa página web foi deployada (foi para a internet) usando `heroku`!
#         """)
#
#     @staticmethod
#     def _git_description():
#         st.markdown("""
#             ### **Git** ###
#
#             Git é um sistema de controle de versões distribuiído, usado em desenvolvimento de software,
#              mas pode ser usado pra registrar o histórico de edições de qualquer tipo de arquivo.
#
#             Uma das plataformas que usa o Git é o `GitHub`, e é amplamente utilizado por programadores para
#             divulgação de seus trabalhos ou para que outros programadores contribuam com o projeto,
#             além de promover fácil comunicação através de recursos que relatam
#             problemas ou mesclam repositórios remotos (issues, pull request).
#
#             O código de programação desta página (e do resto do tutorial) está
#             armazenado num repositório público do `Github`!
#             Para dar uma olhada, só acessar:
#
#             https://github.com/arthurtuio/streamlit-heroku-python-br-2020
#         """)
#
#     @staticmethod
#     def _create_column_names(num_cols=2):
#         nome_colunas = "AB"
#
#         if num_cols == 3:
#             nome_colunas += "C"
#
#         elif num_cols == 4:
#             nome_colunas += "CD"
#
#         elif num_cols == 5:
#             nome_colunas += "CDE"
#
#         return list(nome_colunas)
#
#     @staticmethod
#     def _make_plot(plot_type, chart_data):
#         if plot_type == "bar_chart":
#             return st.bar_chart(chart_data)
#
#         elif plot_type == "area_chart":
#             return st.area_chart(chart_data)
#
#         elif plot_type == "line_chart":
#             return st.line_chart(chart_data)
#
#
if __name__ == '__main__':
    MainPage().initialize()
