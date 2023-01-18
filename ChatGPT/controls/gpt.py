"""
Interface for chatGPT
"""
import view
from flet import *
from view import ChangeRoute
from gpt_control import getCompletion, getModelIDs
from main import _moduleList

text_home = [
        "\"Explain quantum computing in simple terms\"",
        "Remembers what user said earlier in the conversation",
        "May occasionally generate incorrect information",
        "\"Got any creative ideas for a 10 year Old's birthday?\"",
        "Allows user to provide follow-up corrections",
        "May occasionally produce harmful instructions or biased content",
        "\"How do I make an HTTP request in Javascript?\"",
        "Trained to decline inappropriate requests",
        "Limited knowledge of world and events after 2021"
]

class GPTWrite(UserControl):

    def __init__(self):
        self.list_questions = []
        self.list_answers = []
        self.model_davinci = "text-davinci-003"
        self.container = Container(
            bgcolor="#40414f",
            width=600,
            border_radius=6,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Container(
                        alignment=alignment.center,
                        content=TextField(
                            width=500,
                            text_size=14,
                            color=colors.WHITE,
                            border_radius=6,
                            bgcolor="#40414f",
                            border_color="transparent",
                            filled=True,
                            dense=True,
                            cursor_color=colors.WHITE,
                            cursor_width=1,
                            hint_text="Your question...",
                            prefix_icon = icons.QUESTION_MARK,
                            hint_style=TextStyle(size=11, color=colors.BLUE_GREY),
                            keyboard_type=KeyboardType.MULTILINE,
                            min_lines=1,
                            max_lines=4,
                            expand=True,
                            shift_enter=True,
                            on_submit=lambda e: self.onRequest(e),
                            
                        ),
                    ),
                    IconButton(
                        icon=icons.SEND,                        
                        icon_size=20,
                        on_click=lambda e: self.onRequest(e),
                    ),
                ]
            ),

        )
        super().__init__()

    def build(self):
        
        return self.container

    def onRequest(self,e):
        global _moduleList
        for page in e.page.views[:]:
            if page.route == '/chatgpt':
                model = page.controls[0].controls[0].controls[2].controls[0].dropdown.value
                prompt = page.controls[0].controls[0].controls[2].controls[2].container.content.controls[0].content.value

                if model == None:
                    model = self.model_davinci
                ret = getCompletion(model=model, prompt=prompt)
                if ret != None:
                    print(ret)
                    page.controls[0].controls[0].controls[2].controls[1].container.content.controls[0].controls[0].value = ret
                    page.controls[0].controls[0].controls[2].controls[1].container.content.controls[0].controls[0].update()

        



class GPTAnswer(UserControl):
    def __init__(self):
        self.list_questions = []
        self.list_answers = []

        self.model_davinci = "text-davinci-003"
        self.container = Container(
            content=Column(
                expand=True,
                alignment=MainAxisAlignment.END,                    
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Row(
                        controls=[
                            Markdown(
                                "Hey this is a test",
                                selectable=True,
                                extension_set="gitHubWeb",
                                code_theme="tomorrow-night",
                                code_style=TextStyle(font_family="Roboto Mono"),
                                on_tap_link=lambda e: page.launch_url(e.data),width=700)
                        ],
                    ),
                ],
            ),
        )
        super().__init__()

    def build(self):
        return self.container

class GPTParameters(UserControl):
    def __init__(self):
        self.list_questions = []
        self.list_answers = []

        self.model_davinci = "text-davinci-003"
        self.dropdown = Dropdown(
            label="Model",
            hint_text="Choose the model you want to use",
            dense=True,            
        )

        super().__init__()

    def build(self):
        modelIDS=getModelIDs()
        options = [dropdown.Option('') for i in range(len(modelIDS))]
        for i in range(len(modelIDS)):
            options[i] = dropdown.Option(modelIDS[i])
        self.dropdown.options = options
        
        return Container(
            content=self.dropdown,
        )