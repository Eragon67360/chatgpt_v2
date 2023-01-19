# ChatGPT v.2
# Table of contents
+ [About](#about)
+ [Getting Started](#getting_started)
    + [Prerequisites](#prerequisites)
    + [Windows users](#windows)
    + [Linux users](#linux)
+ [How to use](#use)
+ [Notes](#notes)

## About <a name = "about"></a>
An OpenAI-based ChatGPT with more flexibility.

This new version uses Flutter to make the application platform independent.

## Getting Started <a name = "getting_started"></a>

### Prerequisites: <a name = "prerequisites"></a>
    pip install -r requirements.txt
    
You need to have an API key in order to use this application.

Go to [OpenAI](https://beta.openai.com/overview), generate an API key as shown below.

![Profile, API](/assets/images/emploi.png)

![Profile, generate](/assets/images/emploi2.png)



Then, create a file named __API.py__ in the same folder as the file chat.py.

Put the API-key in it.

### Windows users: <a name = "windows"></a>

    Notepad API.py
    
At the beginning of the file, write:

    API_KEY="sk-..."
    
    
### Linux users: <a name = "linux"></a>

    echo 'API_KEY="sk-..."' > API.py


Save your file, you are ready.



## How to use <a name = "use"></a>
Use:

    py chat.py

for a one-time run.

or:

    flet chat.py
    
to modify code and see the changes live.

This little tool replacement gives you the possibility to change the model you want to use.

There will be more evolutions coming and more fine-tuning.

## Notes <a name = "notes"></a>

- The output is shown in such a way that the code is displayed as code, just as the real ChatGPT application would.
- Requests can take time to be transmitted, be patient :)

