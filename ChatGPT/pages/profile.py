"""
Profile page
"""


from flet import *
from controls.navbar import ModernNavBar
from controls.profileData import ProfileData

from view import ShowMenu, ChangeRoute, openDiscord, openHelp, LogOutUser,newChat

def _view_(created_on, last_login, first_name, last_name, email):
    return View(
        '/profile',
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
                            ProfileData(created_on, last_login, first_name, last_name, email),
                        ]
                    )
                ]
            )
        ]
    )