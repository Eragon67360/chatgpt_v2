import flet as ft
from gpt import getCompletion, getModelIDs
import webbrowser
import time

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

def main(page: ft.Page):
    page.window_min_width = 480
    page.window_min_height = 270
    page.window_maximized = True

    page.title = 'ChatGTP v.2'
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    
    list_answers = []

    model_davinci = "text-davinci-003"

    title = ft.Text("ChatGPT v.2",
        size=30,
        bgcolor=None,
        expand=True,
        text_align=ft.TextAlign.CENTER)

    def sendRequest(e):
        model = dropdown.value

        if model == None:
            model = model_davinci
        
        prompt = textfield_question.value + "(generate your answer using markdown)"
        response = ""
        printed_response = ""
        if prompt != "":
            response = getCompletion(model,prompt)
            
            list_answers.append(response)
            textlog.value=str("")
            textlog.update()
        else:
            textlog.value=str("You need to input a question first!")
            textlog.update()
        for i in response:
            printed_response = printed_response+i
            time.sleep(0.02)
            bot_answer.value = printed_response
            bot_answer.update()
                
                
        

    def changeMode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            button_lightmode.text = "Dark Mode"
            button_lightmode.update()
            page.theme_mode = ft.ThemeMode.LIGHT
        else:            
            button_lightmode.text = "Light Mode"
            button_lightmode.update()
            page.theme_mode = ft.ThemeMode.DARK

        page.update()

    def openDiscord(e):
        webbrowser.open('https://discord.com/invite/openai')

    def openHelp(e):
        webbrowser.open('https://help.openai.com/en/')

    button_prompt = ft.IconButton(icon=ft.icons.SEND, on_click=sendRequest,disabled=False)

    button_newchat = ft.TextButton("New Thread", icon=ft.icons.ADD)

    #MENU
    button_lightmode = ft.TextButton("Light Mode", icon=ft.icons.SUNNY, expand=False, on_click=changeMode)
    button_discord = ft.TextButton("OpenAI Discord", icon=ft.icons.DISCORD, on_click=openDiscord)
    button_faq = ft.TextButton("Updates & FAQ", icon=ft.icons.OPEN_IN_NEW, on_click=openHelp)

    modelIDS=getModelIDs()
    options = [ft.dropdown.Option('') for i in range(len(modelIDS))]
    for i in range(len(modelIDS)):
        options[i] = ft.dropdown.Option(modelIDS[i])

    dropdown = ft.Dropdown(
        label="Model",
        hint_text="Choose the model you want to use",
        dense=True,
        options=options
    )
    
    codes_examples = ft.Row(        
        wrap=True,
        expand=False,
        width=800
    )

    menu_container = ft.Column(
                    [                        
                        ft.Column(
                            controls=[
                            button_newchat],
                            expand=True
                        ),
                        dropdown,
                        ft.Divider(),
                        ft.Column(
                            controls=[
                                button_lightmode,
                                button_discord,
                                button_faq
                            ]
                        )
                    ],
                    width=280
                )

    textfield_question = ft.TextField(label="Question",
                                        hint_text='Enter your question here',
                                        value='',
                                        width=900,
                                        height=65,
                                        text_align=ft.TextAlign.LEFT,
                                        on_submit=sendRequest)

    textlog = ft.Text(value="",
        size=12,
        color=ft.colors.RED,
        bgcolor=None)

#     code="1. Open the file.\n\
# 2. Find the following code block on line 21:\n\
# \n\
#         <html>\n\
#           <head>\n\
#             <title>Test</title>\n\
#           </head>\n\
# \n\
# 3. Update the title to match the name of your website."

    bot_answer = ft.Markdown(selectable=True,
                            extension_set="gitHubWeb",
                            code_theme="atom-one-dark",
                            code_style=ft.TextStyle(font_family="Roboto Mono"),
                            on_tap_link=lambda e: page.launch_url(e.data),width=700)

    message_box = ft.Row([
        ft.Container(content=textfield_question),
        ft.Container(content=button_prompt)])

    text_credit = ft.Text(value="Free Research Preview: ChatGPT is optimized for dialogue. Our goal is to make AI systems more natural to interact with, and your feedback will help us improve our systems and make them safer.",
                text_align=ft.TextAlign.CENTER,
                color="#999999"
                )


    page.add(
        ft.Row(
            [
                menu_container,
                ft.VerticalDivider(width=0),
                ft.Container(
                    content=ft.Column(                        
                        controls=[
                            title,
                            codes_examples,
                            bot_answer,
                            textlog,
                            message_box,
                            text_credit
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=5,
                    alignment=ft.alignment.center,
                )
                
            ],
            expand=True,
            spacing=15
        ),        
    )

    page.update()

    for i in range(3):
        codes_examples.controls.append(
            ft.Container(
                content=ft.TextButton(
                    content=ft.Container(
                        content=ft.Text(text_home[3*i], width=350, size=16, text_align=ft.TextAlign.CENTER)
                    )
                ),
                width=250,
                bgcolor="#343541",
                alignment=ft.alignment.center,
                border_radius=ft.border_radius.all(2),
                margin=ft.margin.all(5),
                padding=ft.padding.all(5)
            )
        )
        codes_examples.controls.append(
            ft.Container(
                ft.Text(text_home[3*i+1], width=350, selectable=False, size=16, text_align=ft.TextAlign.CENTER),
                bgcolor="#343541",
                width=250,
                alignment=ft.alignment.top_center,
                border_radius=ft.border_radius.all(2),
                padding=ft.padding.all(5)
                
            )
        )
        codes_examples.controls.append(
            ft.Container(
                ft.Text(text_home[3*i+2], width=350, selectable=False, size=16, text_align=ft.TextAlign.CENTER),
                bgcolor="#343541",
                width=250,
                alignment=ft.alignment.top_center,
                border_radius=ft.border_radius.all(2),
                padding=ft.padding.all(5)
                
            )
        )

    page.update()


    

ft.app(target=main, view=ft.WEB_BROWSER)