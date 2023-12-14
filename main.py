import gradio as gr
def visible_component(input_text):
    return gr.update(visible=True)
def login_fn(username, password):

    # Add your authentication logic here
    gr.update(visible=True)
    if username == "your_username" and password == "your_password":
        return "Login successful!"
    else:
        return "Invalid credentials."

with gr.Blocks() as demo:
    with gr.Column():
        login = gr.Textbox(label="Login")
        password = gr.Textbox(label="Password")
        greet_btn = gr.Button("Log In")
        result = gr.Textbox(label="",visible=False)
        greet_btn.click(fn=login_fn, inputs=[login,password], outputs=result).then(fn=visible_component, inputs= login, outputs= result)

if __name__ == "__main__":
    demo.launch()




