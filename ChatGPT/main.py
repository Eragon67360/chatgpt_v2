from flet import *
import os, importlib.util
from controls.navbar import ModernNavBar
#routing
global _moduleList
_moduleList = {}

for _, dirs, __ in os.walk(r'./'):
    for dir in dirs:
        if dir =='pages':
            for filename in os.listdir(dir):
                _file = os.path.join(dir, filename)

                if os.path.isfile(_file):
                    filename = filename[:-3]

                    _moduleList[
                        "/" + filename
                    ] = importlib.util.spec_from_file_location(filename, _file)

def main(page: Page):
    page.title = 'OpenAI All-In-One'
    page.padding = 0
    page.theme_mode = ThemeMode.DARK
    page.dark_theme = Theme(page_transitions=PageTransitionsTheme.ios)
    
    page.window_min_width = 730
    page.window_min_height = 300

    page.overlay.clear()
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

    page.views.append(
        _moduleList['/login'].loader.load_module()._view_(page)
    )
    
    #set the URL
    page.go("/login")
    page.update()
    pass

if __name__ == '__main__':
    app(target=main)