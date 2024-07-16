#==============================================================================
# extension.py
#==============================================================================
import os
import gradio as gr
from PIL import Image

from modules import script_callbacks

# process_prompt_analysis
def process_prompt_analysis(self, input_image_path):
    tags_list = "hoge"
    return tags_list

# Generate
def Generate(self, input_image_path: str, prompt: str, negative_prompt: str, controlnet_scale: float) -> Image.Image:
    try:
        print(prompt)
        input_image = Image.open(input_image_path)
        # ここで何らかの処理を行う。現状では入力画像をそのまま出力
        output_image = input_image
        return output_image
    except Exception as e:
        print(f"Error in Generate method: {e}")
        return None
    
# on_ui_tabs
def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as gr_ui_sketch2lineart:
        with gr.Row():
            with gr.Column():
                self.input_image_path = gr.Image(label="Input image", type='filepath')
                self.prompt = gr.Textbox(label="Prompt", lines=3)
                self.negative_prompt = gr.Textbox(label="Negative prompt", lines=3, value="sketch, lowres, error, extra digit, fewer digits, cropped, worst quality,low quality, normal quality, jpeg artifacts, blurry")
                prompt_analysis_button = gr.Button("Prompt analysis")
                self.controlnet_scale = gr.Slider(minimum=0.5, maximum=1.25, value=1.0, step=0.01, label="Lineart fidelity")                 
                generate_button = gr.Button(value="Generate", variant="primary")
            with gr.Column():
                self.output_image = gr.Image(type="pil", label="Output image")

            prompt_analysis_button.click(
                self.process_prompt_analysis,
                inputs=[self.input_image_path],
                outputs=self.prompt
            )

            generate_button.click(
                fn=self.Generate,
                inputs=[self.input_image_path, self.prompt, self.negative_prompt, self.controlnet_scale],
                outputs=self.output_image
            )
        return [(gr_ui_sketch2lineart, "sketch2lineart", "extension_sketch2lineart_tab")]

script_callbacks.on_ui_tabs(on_ui_tabs)

# Direct script
if __name__ == "__main__":
    gr_ui_sketch2lineart = on_ui_tabs()
    gr_ui_sketch2lineart.queue()
    gr_ui_sketch2lineart.launch(share=True)

#
