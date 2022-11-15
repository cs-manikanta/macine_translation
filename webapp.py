import streamlit as st

import googletrans 
from googletrans import Translator

st.title('Translator App')

st.header('Our translator will translate from English to language of your choice.')

trans = Translator()

input_text = st.text_area('Enter your text', height = 100)

Target_Language =st.selectbox('Select the target language' , ('Telugu','Hindi','Bengali','Gujarati','Kannada','Malayalam','Marathi','Odia','Punjabi','Tamil','Urdu'))
st.write('You selected: ', Target_Language)

if st.button('Translate'):
    result = trans.translate(input_text, src='en',dest = Target_Language).text
    st.write(result)





