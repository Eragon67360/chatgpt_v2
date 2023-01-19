"""
login page
"""
from flet import *
from controls import inputText
from view import ChangeRoute, LogInUser

def _view_(page:Page):
    page.overlay.append(
        Column(
            opacity=0.1,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text("",size=30,),
                    ]
                ),

            ]
        )
    )
    return View(
        "/login",
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
                        height=500,
                        alignment=alignment.center,
                        border_radius=8,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Divider(height=20, color="transparent"),
                                Text(
                                    "Login",
                                    size=26,
                                    color="#75a99c",
                                    weight="w600"
                                ),
                                Text(
                                    "Use the form below to log into your account",
                                    size=12,
                                    color="#75a99c",
                                    weight="w400"
                                ),
                                Divider(height=40, color="transparent"),
                                Column(
                                    spacing=5,
                                    controls=[
                                        inputText.InputTextField("Email", False, None,lambda e: LogInUser(e)),
                                        inputText.InputTextField("Password", True, True,lambda e: LogInUser(e)),
                                    ]
                                ),
                                Row(
                                    width=300,
                                    alignment=MainAxisAlignment.END,
                                    controls=[
                                        Text(
                                            "Forgot Password?",
                                            color="#75a99c",
                                            weight="bold",
                                            size=10,
                                        )
                                    ]
                                ),
                                Divider(height=5,color=colors.TRANSPARENT),

                                inputText.SignInOption("Log In", lambda e: LogInUser(e)),
                                Divider(height=60,color=colors.TRANSPARENT),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=4,
                                    controls=[
                                        Text(
                                            "Don't have an accounnt?",
                                            color="#75a99c",
                                            size=10,
                                            weight="bold",
                                        ),
                                        Container(
                                            on_click=lambda e: ChangeRoute(e, '/register'),
                                            content=Text(
                                                "Sign up",
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