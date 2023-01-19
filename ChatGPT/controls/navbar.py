"""
Navbar menu
"""

from flet import *

class ModernNavBar(UserControl):
    def __init__(self, func_home,func_new, func_mode, func_discord, func_updates, func_profile, func_logout):
        self.func_home = func_home
        self.func_new = func_new
        self.func_mode = func_mode
        self.func_discord = func_discord
        self.func_updates = func_updates
        self.func_profile = func_profile
        self.func_logout = func_logout

        super().__init__()

    def ContainedIcon(self, icon_name, text, func):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_click=func,
            on_hover=None,
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        selected=False,
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": colors.TRANSPARENT},
                        ),
                    ),
                    Text(
                        value=text,
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    )
                ],
            )
        )

    def build(self):
        return Container(
            alignment=alignment.center,
            padding=10,
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                expand=True,
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.START,
                spacing=5,
                controls=[
                    self.ContainedIcon(icons.HOME, 'Home', self.func_home),
                    self.ContainedIcon(icons.ADD, 'New Chat', self.func_new),
                    self.ContainedIcon(icons.SUNNY, 'Light mode', self.func_mode),                    
                    Divider(color=colors.BLUE_GREY, height=5),
                    self.ContainedIcon(icons.DISCORD, 'OpenAI Discord', self.func_discord),
                    self.ContainedIcon(icons.OPEN_IN_NEW, 'Updates & FAQ', self.func_updates),
                    Divider(color=colors.BLUE_GREY, height=5),
                    self.ContainedIcon(icons.PERSON, 'Profile', self.func_profile),
                    self.ContainedIcon(icons.LOGOUT, 'Logout', self.func_logout),
                ],

            )

        )