#==============================================================================
# webui.py
#==============================================================================
import gradio as gr

# create_ui
def create_ui():
    with gr.Blocks() as gr_ui_main:
        gr.Markdown("WebUI")        
    return gr_ui_main

# Direct script
if __name__ == "__main__":
    gr_ui_main = create_ui()
    gr_ui_main.queue()
    gr_ui_main.launch(share=True)

#==============================================================================
