import streamlit as st

# Mensagem exibida na tela
st.write('Sou servidora pública!')

st.title('Este é o título do app')
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

resposta = st.slider('Informe o grau de satisfação:', min_value=0, max_value=100)
st.write(f'A resposta do usuario foi {str(resposta)}')
