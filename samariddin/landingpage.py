import gradio as gr


def login_fn(user, password, component):
    if user == "aa" and password == "aa":
        component.visible=True
        return "Login successful!", component.visible
    else:
        return "Invalid credentials.", component.visible
      

with gr.Blocks() as demo:
    col1 = gr.Column()
    col2 = gr.Column(visible=False)
    with col1:
        user = gr.Textbox(label="User")
        password = gr.Textbox(label="Password")
        login_btn = gr.Button("Login")
        
        result = gr.Textbox(label="", visible=False)
      
        login_btn.click(login_fn, [user, password], col1).then(lambda :gr.update(visible=True), None, col2).then(lambda :gr.update(visible=False), None, col1)

    with col2:
        gr.Markdown("""
        ## Hush kelibsiz
        """)

if __name__ == "__main__":
    demo.launch()





