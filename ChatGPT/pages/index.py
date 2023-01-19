"""
INDEX
Page displayed when login
"""

from flet import *
from controls.navbar import ModernNavBar
from controls.techChoice import TechChoice
from view import ShowMenu,LogOutUser, ChangeRoute, openDiscord, openHelp,newChat

def _view_(first_name: str, last_name: str):
    return View(
        '/index',
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
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    TechChoice(),
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )