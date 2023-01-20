from flet import *
from controls.navbar import ModernNavBar
from view import ShowMenu,LogOutUser, ChangeRoute, openDiscord, openHelp
from controls.dall_e import Dall_E, Dall_e_Image

def _view_(page):
    page.overlay[0].controls[0].controls[0].value = "DALL·E 2"
    return View(
        '/dalle',
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
                                            None,
                                            lambda e: openDiscord(e),
                                            lambda e: openHelp(e),
                                            lambda e: ChangeRoute(e, '/profile'),
                                            lambda e: LogOutUser(e),
                                        ),
                                    ),
                                ],
                            ),
                            VerticalDivider(width=60, color=colors.YELLOW),
                            Column(
                                expand=True,
                                alignment=MainAxisAlignment.START,
                                horizontal_alignment=CrossAxisAlignment.START,
                                controls=[
                                    Column(
                                        expand=False,
                                        alignment=MainAxisAlignment.START,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            Dall_E(),
                                        ]
                                    ),
                                    Column(
                                        expand=True,
                                        alignment=MainAxisAlignment.START,
                                        # horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            Dall_e_Image(),
                                        ]
                                    )
                                ]),
                            
                        ]
                    )
                ]
            )
        ]
    )