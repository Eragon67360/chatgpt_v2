from flet import *

from gpt_control import getCompletion, getModelIDs
from controls.navbar import ModernNavBar
from controls.gpt import GPTWrite,GPTAnswer,GPTParameters

from view import ShowMenu,LogOutUser, ChangeRoute, openDiscord, openHelp,newChat
import webbrowser
import time

def _view_(page):
    page.overlay[0].controls[0].controls[0].value = "ChatGPT v.2"
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
                                            lambda e: newChat(e),
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
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Column(
                                        alignment=MainAxisAlignment.START,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            GPTParameters(),
                                        ]
                                    ),
                                    Column(
                                        expand=True,
                                        alignment=MainAxisAlignment.END,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            ListView(
                                                expand=1,
                                                spacing=10,
                                                padding=20,
                                                auto_scroll=True,
                                            ),
                                            GPTWrite(),
                                        ],
                                    ),
                                ]
                            ),
                        ]
                    )
                ]
            )
        ]
    )
