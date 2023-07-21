import streamlit as st
from dotenv import load_dotenv
from streamlit_chat import message
import replicate

load_dotenv()

def generate_response(human_input):

	output = replicate.run(
		"replicate/llama70b-v2-chat:e951f18578850b652510200860fc4ea62b3b16fac280f83ff32282f87bbd2e48",
		input={"prompt": human_input},)
	# The replicate/llama70b-v2-chat model can stream output as it's running. 
	# Collect all response parts into a list
	response_parts = []
	for item in output:
		response_parts.append(item)

	response = " ".join(response_parts)

	return response

st.title("🤖 Replicate OpenAI LlamaV2")

if 'generated' not in st.session_state:
	st.session_state['generated'] = []

if 'past' not in st.session_state:
	st.session_state['past'] = []

def get_text():
	input_text = st.text_input(" ", key="input")
	return input_text

user_input = get_text()

if user_input:
	output = generate_response(user_input)
	st.session_state.past.append(user_input)
	st.session_state.generated.append(output)

if st.session_state['generated']:
	for i in range(len(st.session_state['generated'])):
		message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
		message(st.session_state["generated"][i], key=str(i))