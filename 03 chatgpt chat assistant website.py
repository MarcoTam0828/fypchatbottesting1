import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "I want you to act as an AI primary school english tutor. I will provide you with a student who needs help improving their english grammar and your task is to use artificial intelligence tools, such as natural language processing, to give the student feedback on how they can improve their composition. You should also use your rhetorical knowledge and experience about effective writing techniques in order to suggest ways that the student can better express their thoughts and ideas in written form."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Primary English Tutor")

demo.launch(share=True)