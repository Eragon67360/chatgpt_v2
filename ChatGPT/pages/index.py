"""
INDEX
Page displayed when login
"""

from flet import *
from controls import navbar, techChoice
from view import ShowMenu #,PostText, LogUserOut,ChangeRoute

def _view_():
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
                                        bgcolor=colors.WHITE,
                                        width=60,
                                        expand=True,
                                        animate=animation.Animation(35,"decelerate"),
                                        on_hover=lambda e:ShowMenu(e),
                                        content=navbar.ModernNavBar(),
                                    ),
                                ],
                            ),
                            VerticalDivider(width=60, color=colors.TRANSPARENT),
                            Column(
                                expand=True,
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    techChoice.TechChoice(),
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )