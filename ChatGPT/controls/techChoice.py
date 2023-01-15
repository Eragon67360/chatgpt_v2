"""
User can choose a technology to begin with
"""
import view
from flet import *
from view import ChangeRoute


class TechChoice(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            bgcolor=colors.WHITE,
            width=450,
            height=120,
            border_radius=6,
            padding=5,
            alignment=alignment.center,
            
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        alignment=alignment.center,                        
                        content=Column(                            
                            controls=[
                                Container(
                                    content=ElevatedButton(
                                        on_click=None,
                                        content=Text(
                                            "ChatGPT v2",
                                            size=16,
                                            weight="bold",
                                        ),
                                        style=ButtonStyle(
                                            shape={
                                                "": RoundedRectangleBorder(radius=8),
                                            },

                                            color={"": "white",},
                                            bgcolor="#75a99c"
                                            
                                        ),
                                    # height=42,
                                    width=400,
                                    )
                                ),
                                Container(
                                    content=ElevatedButton(
                                        on_click=None,
                                        content=Text(
                                            "DALL·E 2 v.2",
                                            size=16,
                                            weight="bold",
                                        ),
                                        style=ButtonStyle(
                                            shape={
                                                "": RoundedRectangleBorder(radius=8),
                                            },

                                            color={"": "white",}
                                        ),
                                    # height=42,
                                    width=400,
                                    )
                                ),

                            ],
                        )
                    )
                ]
            )
        )