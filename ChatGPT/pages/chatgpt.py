from flet import *

from gpt_control import getCompletion, getModelIDs
from controls.navbar import ModernNavBar
from controls.gpt import GPTWrite,GPTAnswer,GPTParameters

from view import ShowMenu,LogOutUser, ChangeRoute, openDiscord, openHelp
import webbrowser
import time

def _view_():
    return View(
        '/chatgpt',
        controls=[
            Column(
                expand=True,
                controls=[
                    Row(
                        expand=True,
                        controls=[
                            Column(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Container(
                                        # bgcolor=colors.WHITE,
                                        width=60,
                                        expand=True,
                                        animate=animation.Animation(35,"decelerate"),
                                        on_hover=lambda e:ShowMenu(e),
                                        content=ModernNavBar(
                                            lambda e: ChangeRoute(e, '/index'),
                                            None,
                                            lambda e: openDiscord(e),
                                            lambda e: openHelp(e),
                                            lambda e: ChangeRoute(e, '/profile'),
                                            lambda e: LogOutUser(e),
                                        ),
                                    ),
                                ],
                            ),
                            VerticalDivider(width=60, color=colors.TRANSPARENT),
                            Column(
                                expand=True,
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    GPTParameters(),
                                    # Divider(height=500, color=colors.TRANSPARENT),
                                    GPTAnswer(),
                                    # Divider(height=500, color=colors.TRANSPARENT),
                                    GPTWrite(),
                                    
                                ]
                            ),
                            
                        ]
                    )
                ]
            )
        ]
    )



# def main(page: Page):
#     page.window_min_width = 480
#     page.window_min_height = 270
#     page.window_maximized = True

#     page.title = 'ChatGTP v.2'
#     page.appbar = AppBar(
#         title=Text("OpenAI v2"),    # title of the AppBar, with a white color
#         center_title=True,          # we center the title,
#     )
#     page.theme_mode = ThemeMode.DARK
#     page.padding = 0
#     page.spacing = 0
    
    

#     outputs = Row(controls=[
#         Container(
#             content=Column(
#                 wrap=True,
#                 expand=True,
#                 width=1200,),
                
#         )],
#         expand=True,
#         vertical_alignment=CrossAxisAlignment.START,
#         auto_scroll=True,
#         scroll=ScrollMode.ALWAYS,
        
#     )


#     def updateOutputForRequest():
#         outputs.controls[0].content.controls.clear()
#         for i in range(len(list_questions)):
#             outputs.controls[0].content.controls.append(Text(list_questions[i], size=16))
#             if i<(len(list_answers)):

#                 outputs.controls[0].content.controls.append(Markdown(list_answers[i],
#                                         selectable=True,
#                                         extension_set="gitHubWeb",
#                                         code_theme="tomorrow-night",
#                                         code_style=TextStyle(font_family="Roboto Mono"),#expand=True,
#                                         on_tap_link=lambda e: page.launch_url(e.data),width=700))
#         page.update()

#     def updateOutputAfterRequest():
#         outputs.controls[0].content.controls.clear()
#         for i in range(len(list_questions)):
#             outputs.controls[0].content.controls.append(Text(list_questions[i], size=16))            
#             outputs.controls[0].content.controls.append(Markdown(list_answers[i],
#                                     selectable=True,
#                                     extension_set="gitHubWeb",
#                                     code_theme="tomorrow-night",
#                                     code_style=TextStyle(font_family="Roboto Mono"),#expand=True,
#                                     on_tap_link=lambda e: page.launch_url(e.data),width=700))

#         # for i in response:
#         #     printed_response = printed_response+i
#         #     time.sleep(0.02)
#         #     bot_answer.value = printed_response
#         page.update()

#     def sendRequest(e):
#         codes_examples.visible = False
#         page.update()
#         model = dropdown.value
        
#         if model == None:
#             model = model_davinci
        
#         prompt = textfield_question.value + "(generate your answer using markdown)"
#         list_questions.append(textfield_question.value)
        
#         updateOutputForRequest()
#         response = ""
#         printed_response = ""
#         if textfield_question.value != "":
#             textfield_question.value = ""
#             textfield_question.update()
#             response = getCompletion(model,prompt)
#             list_answers.append(response)
#             textlog.value=str("")
#             textlog.update()
#         else:
#             textlog.value=str("You need to input a question first!")
#             textlog.update()
        
#         updateOutputAfterRequest()
        
            

#     def changeMode(e):
#         if page.theme_mode == ThemeMode.DARK:
#             button_lightmode.text = "Dark Mode"
#             button_lightmode.update()
#             page.theme_mode = ThemeMode.LIGHT
#         else:            
#             button_lightmode.text = "Light Mode"
#             button_lightmode.update()
#             page.theme_mode = ThemeMode.DARK

#         page.update()

#     def openDiscord(e):
#         webbrowser.open('https://discord.com/invite/openai')

#     def openHelp(e):
#         webbrowser.open('https://help.openai.com/en/')

#     button_prompt = IconButton(icon=icons.SEND, on_click=sendRequest,disabled=False)

#     button_newchat = TextButton("New Thread", icon=icons.ADD)

#     #MENU
#     button_lightmode = TextButton("Light Mode", icon=icons.SUNNY, expand=False, on_click=changeMode)
#     button_discord = TextButton("OpenAI Discord", icon=icons.DISCORD, on_click=openDiscord)
#     button_faq = TextButton("Updates & FAQ", icon=icons.OPEN_IN_NEW, on_click=openHelp)

#     modelIDS=getModelIDs()
#     options = [dropdown.Option('') for i in range(len(modelIDS))]
#     for i in range(len(modelIDS)):
#         options[i] = dropdown.Option(modelIDS[i])

#     dropdown = Dropdown(
#         label="Model",
#         hint_text="Choose the model you want to use",
#         dense=True,
#         options=options
#     )
    
#     codes_examples = Row(        
#         wrap=True,
#         expand=True,
#         width=800,
        
#     )



#     menu_container = Column(
#                     [                        
#                         Column(
#                             controls=[
#                             button_newchat],
#                             expand=True
#                         ),
#                         dropdown,
#                         Divider(),
#                         Column(
#                             controls=[
#                                 button_lightmode,
#                                 button_discord,
#                                 button_faq
#                             ]
#                         )
#                     ],
#                     width=280
#                 )

#     textfield_question = TextField(label="Question",
#                                         hint_text='Enter your question here',
#                                         value='',
#                                         width=900,
#                                         height=65,
#                                         text_align=TextAlign.LEFT,
#                                         on_submit=sendRequest)

#     textlog = Text(value="",
#         size=12,
#         color=colors.RED,
#         bgcolor=None)

#     bot_answer = Markdown(selectable=True,
#                             extension_set="gitHubWeb",
#                             code_theme="tomorrow-night",
#                             code_style=TextStyle(font_family="Roboto Mono"),
#                             expand=True,
#                             on_tap_link=lambda e: page.launch_url(e.data),width=700)



#     message_box = Row([
#         Container(content=textfield_question),
#         Container(content=button_prompt)])

#     text_credit = Text(value="Free Research Preview: ChatGPT is optimized for dialogue. Our goal is to make AI systems more natural to interact with, and your feedback will help us improve our systems and make them safer.",
#                 text_align=TextAlign.CENTER,
#                 color="#999999"
#                 )


#     page.add(
#         Row(
#             [
#                 menu_container,
#                 VerticalDivider(width=0),
#                 Container(
#                     content=Column(                        
#                         controls=[
#                             codes_examples,
#                             outputs,
#                             textlog,
#                             message_box,
#                             text_credit
#                         ],
#                         horizontal_alignment=CrossAxisAlignment.CENTER
#                     ),
#                     padding=5,
#                     alignment=alignment.center,
#                 )
                
#             ],
#             expand=True,
#             spacing=15
#         ),        
#     )

#     page.update()

    

#     for i in range(3):
#         codes_examples.controls.append(
#             Container(
#                 content=TextButton(
#                     content=Container(
#                         content=Text(text_home[3*i], width=350, size=16, text_align=TextAlign.CENTER)
#                     )
#                 ),
#                 width=250,
#                 bgcolor="#343541",
#                 alignment=alignment.center,
#                 border_radius=border_radius.all(2),
#                 margin=margin.all(5),
#                 padding=padding.all(5)
#             )
#         )
#         codes_examples.controls.append(
#             Container(
#                 Text(text_home[3*i+1], width=350, selectable=False, size=16, text_align=TextAlign.CENTER),
#                 bgcolor="#343541",
#                 width=250,
#                 alignment=alignment.top_center,
#                 border_radius=border_radius.all(2),
#                 padding=padding.all(5)
                
#             )
#         )
#         codes_examples.controls.append(
#             Container(
#                 Text(text_home[3*i+2], width=350, selectable=False, size=16, text_align=TextAlign.CENTER),
#                 bgcolor="#343541",
#                 width=250,
#                 alignment=alignment.top_center,
#                 border_radius=border_radius.all(2),
#                 padding=padding.all(5)
                
#             )
#         )

#     page.update()


    

# app(target=main, view=WEB_BROWSER, web_renderer='html')