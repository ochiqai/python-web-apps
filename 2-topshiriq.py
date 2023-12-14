import gradio as gr
def visible_component(input_text):
    return gr.update(visible=True)
def login_fn(username, password):

    # Add your authentication logic here
    gr.update(visible=True)
    if username == "aa" and password == "aa":

        return "Login successful!"
    else:
        return "Invalid credentials."

with gr.Blocks() as demo:
    col1 = gr.Column()
    col2 = gr.Column(visible=False)
    with col1:
        login = gr.Textbox(label="Login")
        password = gr.Textbox(label="Password")
        greet_btn = gr.Button("Log In")
        result = gr.Textbox(label="",visible=False)
        greet_btn.click(lambda :gr.update(visible=False), None, col1).then(lambda :gr.update(visible=True), None, col2)

    with col2:
        gr.Markdown("""
        ## Hush kelibsiz
        """)

if __name__ == "__main__":
    demo.launch()




