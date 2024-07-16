def ui_tabs_callback():
    res = []

    for c in ordered_callbacks('ui_tabs'):
        try:
            res += c.callback() or []
        except Exception:
            report_exception(c, 'ui_tabs_callback')

    return res

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
