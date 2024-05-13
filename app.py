from openai import OpenAI
import streamlit as st

class ChatApp:
    def __init__(self, openai_api_key, model, initial_prompt):
        self.client = OpenAI(api_key=openai_api_key)
        self.model = model
        self.system_prompt = initial_prompt
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def get_stress_analysis(self):
        stress_analysis_prompt = "Analyze the following conversation to identify potential stressors and provide actionable solutions to alleviate stress:\n\n"
        for message in st.session_state.messages:
            stress_analysis_prompt += f"{message['role'].capitalize()}: {message['content']}\n"
        stress_analysis_prompt += "Stress Analysis:"

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a stress analyzer"},
                {"role": "user", "content": stress_analysis_prompt}
            ],
            temperature=0.7,
        )
        stress_analysis = response.choices[0].message.content

        return stress_analysis

    def display_and_handle_input(self):
        prompt = st.chat_input("Talk with me")
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        if prompt:
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            conversation_history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            with st.chat_message("assistant"):
                stream = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": self.system_prompt}
                    ] + conversation_history,
                    stream=True,
                )
                response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})




with st.sidebar:
    st.header('Healthcare Assistant', divider='violet')
    openai_api_key = st.text_input("Enter your API key")
    model = st.selectbox("Choose chat model", ("gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-2024-04-09"))


initial_prompt = '''
    You are a therapist and caring healthcare assistant, dedicated to recognizing stress and offering emotional support to those who need it. Your mission is to create a safe and understanding environment where people can freely share their feelings and worries.
    *Guidelines*
    - Always communicate with an empathetic and warm tone, using appropriate emojis to convey your care and support.
    - Pay close attention to the individual's needs and tailor your responses accordingly, ensuring that they feel heard and valued.
    - Offer gentle guidance and helpful suggestions to support their emotional well-being and create a positive atmosphere.
    - Avoid judgmental or harsh language, fostering an open and accepting space for individuals to express themselves freely.
    - Encourage self-reflection and personal growth, empowering individuals to overcome challenges and embrace a more fulfilling life.
    - Be engaging and keep the conversation flowing by asking open-ended questions and actively listening to the individual's responses.
    - Continuously adapt your approach based on the individual's unique needs and maintain a genuine interest in their well-being, demonstrating that you're there for them every step of the way.
            '''
if openai_api_key:
    app = ChatApp(openai_api_key, model, initial_prompt)
    app.display_and_handle_input()
    with st.sidebar:
        if st.button("Analyze"):
            with st.spinner('Analyzing...'):
                stress_analysis = app.get_stress_analysis()
                st.write(stress_analysis)