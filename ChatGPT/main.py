from flet import flet, Page,ThemeMode
import os, importlib.util

#routing
global _moduleList
_moduleList = {}

#os.walk() to gt the data of home
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

    page.theme_mode = ThemeMode.DARK

    page.views.append(
        _moduleList['/login'].loader.load_module()._view_()
    )

    #set the URL
    page.go("/login")
    page.update()
    pass

if __name__ == '__main__':
    flet.app(target=main)