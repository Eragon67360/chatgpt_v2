"""
Profile data page
"""

from flet import *

class ProfileData(UserControl):
    def __init__(self, created_on, last_login, first_name, last_name, email):
        self.created_on = created_on
        self.last_login = last_login
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        super().__init__()

    def ReturnText(self, name, size):
        return Text(
            value=name,
            size=size,
            weight="bold"
        )

    def build(self):
        return Column(
            expand=True,
            horizontal_alignment=CrossAxisAlignment.START,
            controls=[
                Divider(height=30, color=colors.TRANSPARENT),
                Row(
                    controls=[
                        Text(
                            "User Profile",
                            size=25,
                            weight=FontWeight.BOLD,
                        )
                    ]
                ),
                Divider(height=10),
                Divider(height=20, color=colors.TRANSPARENT),
                #Container with time infos
                Container(
                    width=400,
                    content=Row(
                        alignment=MainAxisAlignment.START,
                        spacing=40,
                        controls=[
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("User created on", 10),
                                    self.ReturnText(self.created_on, 12),
                                ]
                            ),
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("Last login", 10),
                                    self.ReturnText(self.last_login, 12),
                                ]
                            )
                        ]
                    )
                ),
                Divider(height=20, color=colors.TRANSPARENT),
                #Container with user names
                Container(
                    width=400,
                    content=Row(
                        alignment=MainAxisAlignment.START,
                        spacing=40,
                        controls=[
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("First Name", 10),
                                    self.ReturnText(self.first_name, 12),
                                ]
                            ),
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("Last Name", 10),
                                    self.ReturnText(self.last_name, 12),
                                ]
                            )
                        ]
                    )
                ),
                Divider(height=20, color=colors.TRANSPARENT),
                #Container with email
                Container(
                    width=400,
                    content=Row(
                        alignment=MainAxisAlignment.START,
                        spacing=40,
                        controls=[
                            Column(
                                spacing=2,
                                controls=[
                                    self.ReturnText("Email", 10),
                                    self.ReturnText(self.email, 12),
                                ]
                            ),
                        ]
                    )
                )
            ]

        )