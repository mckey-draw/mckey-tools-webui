#
from modules import extensions

@dataclasses.dataclass
class ScriptCallback:
    script: str
    callback: any
    name: str = "unnamed"

def add_callback(callbacks, fun, *, name=None, category='unknown', filename=None):
    if filename is None:
        stack = [x for x in inspect.stack() if x.filename != __file__]
        filename = stack[0].filename if stack else 'unknown file'

    extension = extensions.find_extension(filename)
    extension_name = extension.canonical_name if extension else 'base'

    callback_name = f"{extension_name}/{os.path.basename(filename)}/{category}"
    if name is not None:
        callback_name += f'/{name}'

    unique_callback_name = callback_name
    for index in range(1000):
        existing = any(x.name == unique_callback_name for x in callbacks)
        if not existing:
            break

        unique_callback_name = f'{callback_name}-{index+1}'

    callbacks.append(ScriptCallback(filename, fun, unique_callback_name))

callback_map = dict(
    callbacks_ui_tabs=[],
)

#
def on_ui_tabs(callback, *, name=None):
    """register a function to be called when the UI is creating new tabs.
    The function must either return a None, which means no new tabs to be added, or a list, where
    each element is a tuple:
        (gradio_component, title, elem_id)

    gradio_component is a gradio component to be used for contents of the tab (usually gr.Blocks)
    title is tab text displayed to user in the UI
    elem_id is HTML id for the tab
    """
    add_callback(callback_map['callbacks_ui_tabs'], callback, name=name, category='ui_tabs')
