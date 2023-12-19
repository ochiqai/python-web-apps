import gradio as gr


def visible_component():
    return gr.update(visible=True)


def login_fn(username, password):
    gr.update(visible=True)
    if username == "1" and password == "1":
        return "Login successful!"
    else:
        return "Invalid credentials."


with gr.Blocks() as demo:
    with gr.Column():
        user = gr.Textbox(label="User")
        password = gr.Textbox(label="Password")
        login_btn = gr.Button("Log In")

        result = gr.Textbox(label="", visible=False)

        login_btn.click(fn=login_fn, inputs=[user, password], outputs=result).then(fn=visible_component, outputs=result)
if __name__ == "__main__":
    demo.launch()