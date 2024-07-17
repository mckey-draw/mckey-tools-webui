#==============================================================================
# webui.py
#==============================================================================
import gradio as gr

# webui
def webui():
    with gr.Blocks() as gr_ui_main:
        gr.Markdown("WebUI")        
    return gr_ui_main

# Direct script
if __name__ == "__main__":
    gr_ui_main = webui()
    gr_ui_main.queue()
    gr_ui_main.launch(share=True)

#==============================================================================
