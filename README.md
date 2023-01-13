# ChatGPT v.2
An OpenAI-based ChatGPT with more flexibility.

This new version uses Flutter to make the application platform independent.

## Installation
    pip install -r requirements.txt
    
You need to have an API key in order to use this application.

Go to [OpenAI](https://beta.openai.com/overview), generate an API key as shown below.

![Profile, API](/assets/images/emploi.png)

![Profile, generate](/assets/images/emploi2.png)



Then, create a file named __API.py__ in the same folder as the file chat.py.

Put the API-key in it.

### Windows-users:

    Notepad API.py
    
At the beginning of the file, write:

    API_KEY="sk-..."
    
    
### Linux users:

    echo 'API_KEY="sk-..."' > API.py


Save your file, you are ready.



## How to use
Use:

    py chat.py

for a one-time run.

or:

    flet chat.py
    
to modify code and see the changes live.

This little tool replacement gives you the possibility to change the model you want to use.

There will be more evolutions coming and more fine-tuning.

## Notes

- The output is shown in such a way that the code is displayed as code, just as the real ChatGPT application would.
- Requests can take time to be transmitted, be patient :)

