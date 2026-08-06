import gradio as gr

def greet(name):
    return f"Hello {name} 🚀"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(
        placeholder="Enter your name"
    ),
    outputs=gr.Textbox(),
    title="Greeting App"
)

demo.launch()


# ctrl + C : Keyboard interruption in main thread... closing server.