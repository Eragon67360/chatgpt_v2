import openai
from openapi_schema_to_json_schema import to_json_schema
import API
from PIL import Image as pil_img
import requests
import time
from io import BytesIO

openai.api_key = API.API_KEY
from flet import *

def getImage(prompt, amount=1,size="256x256"):
    if amount is None:
        amount=1
    if size is None:
        size="256x256"
    response = openai.Image.create(
        prompt=prompt,
        n=amount,
        size=size,
        )
    urls = ['' for i in range(len(response['data']))]
    for i in range(len(response['data'])):
        urls[i] = response['data'][i]['url']


    return urls

def urlToImage(e,url):    

    if len(url)>1:
        text = "Here are the images I have generated for you:"
    else:
        text = "Here is the image I have generated for you:"
    
    outputed_text = ""


    global _moduleList
    for page in e.page.views[:]:
        if page.route == '/dalle':
            for i in text:
                outputed_text = outputed_text + i
                page.controls[0].controls[0].controls[2].controls[1].controls[0].container.content.controls[1].value = outputed_text
                page.controls[0].controls[0].controls[2].controls[1].controls[0].container.content.controls[1].update()
                time.sleep(0.01)

            image_array = [None for i in range(len(url))]
            for i in range(len(image_array)):
                image_array[i] = Container(
                                content=ShaderMask(
                                    content=Image(
                                        src=url[i],
                                        width=250,
                                        height=250,
                                        fit=ImageFit.CONTAIN,
                                        border_radius=border_radius.all(15),
                                    ),
                                    blend_mode=BlendMode.DST_IN,
                                    shader=LinearGradient(
                                        begin=alignment.top_center,
                                        end=alignment.bottom_center,
                                        colors=[colors.WHITE, colors.TRANSPARENT],
                                        stops=[1.0,1.0],
                                    ),
                                    border_radius=10,
                                ),
                                on_hover=imageHovered,
                                on_click=imageClicked,
                            )
                
            page.controls[0].controls[0].controls[2].controls[1].controls[0].container.content.controls[3].controls[0].controls.clear()
            for i in range(len(image_array)):
                page.controls[0].controls[0].controls[2].controls[1].controls[0].container.content.controls[3].controls[0].controls.append(image_array[i])
                page.controls[0].controls[0].controls[2].controls[1].controls[0].container.content.controls[3].update()
            print(len(page.controls[0].controls[0].controls[2].controls[1].controls[0].container.content.controls[3].controls[0].controls))
            e.page.update()
                
def imageHovered(e):
    e.control.content.shader.stops=[0.2, 1.0] if e.data == "true" else [1.0, 1.0]
    e.control.content.update()

def imageClicked(e):
    url = e.control.content.content.src
    response = requests.get(url)
    
    img = pil_img.open(BytesIO(response.content))
    img.show()