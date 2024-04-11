import streamlit as st
from langchain_google_genai.llms import GoogleGenerativeAI
st.title('🦜🔗 LaGoSt App : Built with Langchain Google Gemini Streamlit')
st.sidebar.title("LaGoSt App")
openai_api_key = st.sidebar.text_input('Input Your Google Studio Gemini API Key. If you do not have you can create for free\
                                       from here https://aistudio.google.com/app/apikey')
st.sidebar.divider()  # 👈 Draws a horizontal rule

st.sidebar.markdown("👋 Hi, Thank you for checking my app. My name is James. Connect with me if you are looking for Generative AI developer.\
                 My Tech stack is : Langchain for LLM Framework, Google Vertex or OpenAI for LLM, StreamLit for frontend. https://www.linkedin.com/in/mascarenhasjames")

def generate_response(input_text):
  llm = GoogleGenerativeAI(model="gemini-1.0-pro-latest", google_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'I am a software developer. Roast Me.')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key:
    st.warning('Please enter your Gemini API Key OR create for free  https://aistudio.google.com/app/apikey', icon='⚠')
  if submitted and openai_api_key:
    generate_response(text)