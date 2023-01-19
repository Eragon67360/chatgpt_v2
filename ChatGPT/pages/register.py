"""
Register page
"""

from flet import *
from controls import inputText
from view import ChangeRoute, Registeruser

def _view_(page):
    page.overlay[0].controls[0].controls[0].value = ""
    return View(
        "/register",
        horizontal_alignment=CrossAxisAlignment.CENTER,
        vertical_alignment=MainAxisAlignment.CENTER,
        controls=[
            Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        bgcolor=colors.WHITE,
                        width=350,
                        height=600,
                        alignment=alignment.center,
                        border_radius=8,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Divider(height=20, color="transparent"),
                                Text(
                                    "Register Form",
                                    size=26,
                                    color="#75a99c",
                                    weight="w600"
                                ),
                                Text(
                                    "Use the form below to create a new account",
                                    size=12,
                                    color="#75a99c",
                                    weight="w400"
                                ),
                                Divider(height=40, color="transparent"),
                                Column(
                                    spacing=5,
                                    controls=[
                                        inputText.InputTextField("First Name", False, None, lambda e: Registeruser(e)),
                                        inputText.InputTextField("Last Name", False, None, lambda e: Registeruser(e)),
                                        inputText.InputTextField("Email", False, None, lambda e: Registeruser(e)),
                                        inputText.InputTextField("Password (min. 6 characters)", True, True, lambda e: Registeruser(e)),
                                    ]
                                ),
                               
                                Divider(height=5,color=colors.TRANSPARENT),

                                inputText.SignInOption("Sign up", lambda e: Registeruser(e)),
                                Divider(height=60,color=colors.TRANSPARENT),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=4,
                                    controls=[
                                        Text(
                                            "Already have an account?",
                                            color="#75a99c",
                                            size=10,
                                            weight="bold",
                                        ),
                                        Container(
                                            on_click=lambda e: ChangeRoute(e, '/login'),
                                            content=Text(
                                                "Sign in",
                                                color=colors.BLUE_900,
                                                size=10,
                                                weight="bold"
                                            )                                        
                                        )
                                    ]
                                    
                                )
                            ]
                        )
                    ),
                    #Footer
                    Column(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            Divider(height=60, color=colors.TRANSPARENT),
                            inputText.GetFooter(),
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Text(
                                        "© Thomas M.",
                                        color=colors.WHITE,
                                        size=10,
                                        weight="w500"
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )