"""
Interface for chatGPT
"""
import time
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
                    ProgressRing(
                        width=16,
                        height=16,
                        stroke_width = 2,
                        visible=False,
                    ),
                    IconButton(
                        icon=icons.SEND,
                        tooltip="Send request",
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
                
                # model value chosen in dropdown
                model = page.controls[0].controls[0].controls[2].controls[0].controls[0].dropdown.value

                # section for the answer+question asked
                display = page.controls[0].controls[0].controls[2].controls[1].controls[0].controls

                input_field = page.controls[0].controls[0].controls[2].controls[1].controls[1].container.content.controls[0].content
                input = input_field.value

                if input == "":
                    e.page.show_snack_bar(SnackBar(content=Text("Please insert text", color=colors.RED), open=True, bgcolor="#474855"))
                else:
                    # Make progress ring visible
                    page.controls[0].controls[0].controls[2].controls[1].controls[1].container.content.controls[1].visible = True
                    page.controls[0].controls[0].controls[2].controls[1].controls[1].container.content.update()

                    answer_container = GPTAnswer()
                    answer_container.container.content.controls[0].content.controls[0].value = input
                    output_field = answer_container.container.content.controls[1].content.controls[2]
                    
                    display.append(answer_container)
                    page.controls[0].controls[0].controls[2].controls[1].update()

                    prompt = input + "(generate your answer using markdown)"
                    self.list_questions.append(input)
                    input_field.value = ""
                    input_field.read_only = True
                    input_field.update()
                    
                    if model == None:
                        model = self.model_davinci
                    ret = getCompletion(model=model, prompt=prompt)
                    
                    if ret != None:
                        self.list_answers.append(ret)
                        page.controls[0].controls[0].controls[2].controls[1].controls[1].container.content.controls[1].visible = False
                        page.controls[0].controls[0].controls[2].controls[1].controls[1].container.content.update()

                        text_outputed =  ""
                        for i in ret:
                            text_outputed = text_outputed + i
                            output_field.value = text_outputed
                            output_field.update()
                            time.sleep(0.01)

                        input_field.read_only = False
                        input_field.update()
                        answer_container.container.content.controls[1].content.padding = 15
                        answer_container.container.content.update()
                        answer_container.container.content.controls[0].update()
                        page.controls[0].controls[0].controls[2].controls[0].update()
                        page.update()

class GPTAnswer(UserControl):
    def __init__(self):
        self.list_questions = []
        self.list_answers = []

        self.model_davinci = "text-davinci-003"
        self.container = Container(            
            content=Column(
                
                controls=[
                    Container(
                        padding=5,
                        content=Row(                        
                            alignment=MainAxisAlignment.END,
                            controls=[                                
                                Text(
                                    size=14,
                                ),
                                Divider(height=5),
                                Icon(icons.PERSON),
                            ]
                        )
                    ),
                    Container(
                        padding=10,
                        bgcolor="#444654",
                        content=Row(                            
                            controls=[
                                Icon(icons.LIGHTBULB),
                                Divider(height=5),
                                Markdown(                                    
                                    selectable=True,
                                    extension_set="gitHubWeb",
                                    code_theme="tomorrow-night",
                                    code_style=TextStyle(font_family="Roboto Mono"),
                                    on_tap_link=lambda e: page.launch_url(e.data),width=700)
                            ],
                        ),
                    )
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
        # temperature=0, max_tokens=2048,top_p=1, frequency_penalty=0.0, presence_penalty=0.0
        return Container(
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.dropdown,
                    Column(
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[                            
                            Text("Temperature", size=15),
                            Slider(
                                active_color="#75a99c",
                                min=0,
                                max=1.0,
                                divisions=10,
                                label="{value}", 
                                ),
                        ]
                    ),
                    Column(
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[                            
                            Text("Max tokens", size=15),
                            Slider(
                                active_color="#75a99c",
                                min=1,
                                max=2049,
                                divisions=2048,
                                label="{value}", 
                                ),
                        ]
                    ),
                ]
            )
            
        )