from flet import *

text = " \
# DALL·E 2\
\n\
\n\
\n\
\n\
```python\n\
    from Nowhere import Dall-E\n\
```\
    "

class Dall_E(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            alignment=alignment.center,
            content=Markdown(text,
            selectable=True,
            extension_set="gitHubWeb",
            code_theme="tomorrow-night",            
            code_style=TextStyle(font_family="Roboto Mono"),
            on_tap_link=lambda e: page.launch_url(e.data),width=700)

        )