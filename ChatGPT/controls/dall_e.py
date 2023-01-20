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

from dall_e_control import getImage, urlToImage

sizes = ["256x256", "512x512", "1024x1024"]


class Dall_E(UserControl):
    def __init__(self):
        size = [dropdown.Option('') for i in range(len(sizes))]
        for i in range(len(sizes)):
            size[i] = dropdown.Option(sizes[i])

        amount = [dropdown.Option(f'{i}') for i in range(1,11)]
        

        self.container = Container(
            content=Row(
                controls=[
                    Container(
                    bgcolor=colors.WHITE,
                    width=600,
                    border_radius=6,
                    content=
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=TextField(
                                        width=500,
                                        text_size=14,
                                        color=colors.BLACK,
                                        border_radius=6,
                                        bgcolor=None,
                                        border_color="transparent",
                                        filled=True,
                                        dense=True,
                                        cursor_color=colors.BLACK54,
                                        cursor_width=1,
                                        hint_text="An Impressionist oil painting of sunflowers in a purple vase...",
                                        hint_style=TextStyle(size=13, color=colors.BLACK38),
                                        keyboard_type=KeyboardType.TEXT,
                                        on_submit=lambda e: self.onRequest(e),
                                        expand=True,                           
                                        on_focus=None,
                                    ),
                                ),
                                ProgressRing(
                                    width=18,
                                    height=18,
                                    stroke_width = 2,
                                    color="#75a99c",
                                    visible=False,
                                ),
                                VerticalDivider(width=10),
                                Container(                        
                                    expand=True,
                                    border_radius=border_radius.horizontal(right=6),
                                    alignment=alignment.center,
                                    bgcolor=colors.BLACK,
                                    height=55,
                                    padding=0,
                                    content=TextButton(                            
                                        expand=True,
                                        content=Text("Generate",color=colors.WHITE,size=13,),
                                        on_click=lambda e: self.onRequest(e),
                                    ),
                                ),
                            ]
                        ),
                    ),
                    Dropdown(label="Number of images generated",hint_text="Number between 1 and 10", options=amount),
                    Dropdown(label="Size",hint_text="Size of the image(s) generated", options=size)
                ]
            )
        )
        
            
        
        super().__init__()

    def build(self):
        return self.container

    def onRequest(self,e,prompt="black cat"):
        # make progressring visible
        for page in e.page.views[:]:
            if page.route == '/dalle':
                page.controls[0].controls[0].controls[2].controls[0].controls[0].container.content.controls[0].content.controls[1].visible = True
                page.controls[0].controls[0].controls[2].controls[0].controls[0].container.content.controls[0].content.controls[1].update()
                prompt = page.controls[0].controls[0].controls[2].controls[0].controls[0].container.content.controls[0].content.controls[0].content.value
                page.controls[0].controls[0].controls[2].controls[0].controls[0].container.content.controls[0].content.controls[0].content.read_only = True
                page.controls[0].controls[0].controls[2].controls[0].controls[0].container.content.controls[0].content.controls[0].content.update()

                if prompt == "":
                    e.page.show_snack_bar(SnackBar(content=Text("Please insert text", color=colors.RED), open=True, bgcolor="#474855"))
                    
                else:
                    amount = page.controls[0].controls[0].controls[2].controls[0].controls[0].container.content.controls[1].value                    
                    size = page.controls[0].controls[0].controls[2].controls[0].controls[0].container.content.controls[2].value
                    if amount is None:
                        amount = 1
                    else:
                        amount = int(amount)
                    url = getImage(prompt=prompt, amount=amount, size=size)
                    urlToImage(e,url)
        page.controls[0].controls[0].controls[2].controls[0].controls[0].container.content.controls[0].content.controls[0].content.read_only = False
        page.controls[0].controls[0].controls[2].controls[0].controls[0].container.content.controls[0].content.controls[0].content.update()
        page.controls[0].controls[0].controls[2].controls[0].controls[0].container.content.controls[0].content.controls[1].visible = False
        page.controls[0].controls[0].controls[2].controls[0].controls[0].container.content.controls[0].content.controls[1].update()


class Dall_e_Image(UserControl):
    def __init__(self):
        self.container = Container(
            content=Column(
                expand=False,
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Divider(height=20, color=colors.TRANSPARENT),
                    Text(size=15, color=colors.WHITE),
                    Divider(height=20, color=colors.WHITE),
                    Column(
                        controls=[
                            GridView(
                                expand=False,
                                runs_count=5,
                                max_extent=250,
                                child_aspect_ratio=1.0,
                                spacing=5,
                                run_spacing=5,
                                ),
                            Divider(height=20, color=colors.GREEN),
                        ],                        
                    )
                ]
            )
        )
        super().__init__()

    def build(self):
        return self.container
        