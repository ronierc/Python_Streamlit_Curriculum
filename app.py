from pathlib import Path
import streamlit as st
from PIL import Image

#Configurações Estruturais #
diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd() #Retorna o diretorio raiz
arquivo_css = diretorio / "styles" / "geral.css"
arquivo_pdf = diretorio / "assets" / "Curriculum.pdf"
arquivo_img = diretorio / "assets" / "foto.png"

#Configuração Geral das Informações

TITULO = "Curriculum | Ronier Cavalari"
NOME = "Ronier Cavalari"
DESCRICAO = """
    Programador FullStack e Analista de Sistemas
"""
EMAIL = "ronier.cavalari@gmail.com"
MIDIA_SOCIAL = {
    "LinkedIn" : "https://www.linkedin.com/in/ronier-cavalari/",
    "GitHub" : "https://github.com/ronierc/",
    "Instagram" : "https://www.instagram.com/ronier.cavalari/"
}
CURSOS = {
    ":dart: Etec de Fernandópolis" : "https://etecfernandopolis.com.br/",
    ":dart: Fundação Educacional de Fernandópolis" : "https://fef.br/"
}

st.set_page_config(
    page_title=TITULO
)

# Carregando Assets 
with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)
with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()
imagem = Image.open(arquivo_img)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(imagem, width=250)
with col2:
    st.title(NOME)
    st.write(DESCRICAO)
    st.download_button(
        label="Download Curriculum",
        data=pdfLeitura,
        file_name=arquivo_pdf.name,
        mime="application/octet-stream"
    )
    st.write(":email:",EMAIL)

# Mídias Sociais
st.write("#")
colunas = st.columns(len(MIDIA_SOCIAL), vertical_alignment="center")
for indice, (plataforma, link) in enumerate(MIDIA_SOCIAL.items()):
    colunas[indice].write(f"[{plataforma}]({link})")

# Experiências 
st.write("#")
st.subheader("Experiências")
st.write("""
    - :chart: Analista de Sistemas
    - :chart: Técnico Residente
    - :chart: Auxiliar Administrativo
    - :chart: Programador
""")


# Skills 
st.write("#")
st.subheader("Skills")
st.code("""
def language(name):
    print ("Python!")
        
function language(name) {
    console.log("HTML, CSS, JavaScript!");
}     
        
function language($name) {
    echo "PHP!";
}
""", language="json")

# Histórico de Trabalho 
st.write("#")
st.subheader("Histórico de Trabalho")
st.write("---")

st.badge("👨‍💻 Analista de Sistemas | SupraSys", color="violet")
st.write("12/2019 - Atualmente")
st.write("""
    Analista de Sistemas atualmente no setor de implanação de software.
         
""")

st.badge("👨‍💻 Técnico Residente | IT2b", color="violet")
st.write("06/2016 - 12/2019")
st.write("""
    Técnico responsável pela rede, impressora, manutenção de computadores, etc.
         
""")

st.badge("👨‍💻 Estagiário - Auxiliar Administrativo | Etec Fernandópolis", color="violet")
st.write("11/2014 - 06/2016")
st.write("""
    Auxiliar Administrativo
         
""")

st.badge("👨‍💻 Desenvolvedor Web | Custommize", color="violet")
st.write("03/2014 - 11/2014")
st.write("""
    Desenvolvedor Full Stack PHP/CSS/JS.
         
""")

st.badge("👨‍💻 Professor Informática | AEComp", color="violet")
st.write("01/2012 - 09/2012")
st.write("""
    Professor de Excel, AutoCad, Corel, Photoshop, Pacote Office, etc.
         
""")

# Cursos
st.write("#")
st.subheader("Cursos")
st.write("---")
for curso, link in CURSOS.items():
    st.write(f"[{curso}]({link})")