import openai
from openapi_schema_to_json_schema import to_json_schema
import API

openai.api_key = API.API_KEY

def getModelIDs():
    models = openai.Model.list()

    jsonschema = to_json_schema(models)

    data = jsonschema['data']

    listModels = ['' for i in range(len(data))]

    for i in range(len(data)):
        listModels[i] = data[i]['id']
    return listModels


def getCompletion(model, prompt, temperature=0, max_tokens=100,top_p=1, frequency_penalty=0.0, presence_penalty=0.0, stop=None):
    completion = openai.Completion.create(
        
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=None
        )

    response = completion.choices[0].text
    return response