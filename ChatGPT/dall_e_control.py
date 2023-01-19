import openai
from openapi_schema_to_json_schema import to_json_schema
import API
from PIL import Image
import requests
import time
from io import BytesIO

openai.api_key = API.API_KEY


def getImage(prompt, amount=1,size="1024x1024"):
    response = openai.Image.create(
        prompt=prompt,
        n=amount,
        size=size,
        )

    url = response['data'][0]['url']
    return url

def urlToImage(e,url):    
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    text = "Here is the image I have generated for you:"
    outputed_text = ""
    global _moduleList
    for page in e.page.views[:]:
        if page.route == '/dalle':
            for i in text:
                outputed_text = outputed_text + i
                page.controls[0].controls[0].controls[2].controls[1].container.content.controls[1].value = outputed_text
                page.controls[0].controls[0].controls[2].controls[1].container.content.controls[1].update()
                time.sleep(0.01)

            
            page.controls[0].controls[0].controls[2].controls[1].container.content.controls[3].src = url
            page.controls[0].controls[0].controls[2].controls[1].container.content.controls[3].update()
