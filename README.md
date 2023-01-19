# ChatGPT v.2
# Table of contents
+ [About](#about)
+ [Getting Started](#getting_started)
    + [Prerequisites](#prerequisites)
    + [Windows users](#windows)
    + [Linux users](#linux)
+ [How to use](#use)
+ [ChatGPT v.2](#chat)
+ [DALL·E 2 v.2](#dalle)
+ [Notes](#notes)

## About <a name = "about"></a>
An OpenAI-based ChatGPT and DALL·E 2 with more flexibility.

This project uses Flutter to make the application platform independent.

## Getting Started <a name = "getting_started"></a>

### Prerequisites: <a name = "prerequisites"></a>
    pip install -r requirements.txt
    
You need to have an API key in order to use this application.

Go to [OpenAI](https://beta.openai.com/overview), generate an API key as shown below.

![Profile, API](/assets/images/emploi.png)

![Profile, generate](/assets/images/emploi2.png)



Then, create a file named __API.py__ in the same folder as the file main.py.

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

    py main.py

for a one-time run.

or:

    flet main.py
    
to modify code and see the changes live.

Fist you have to create an account to use this tool.

The Authentication system is based on Firebase (pyrebase, library for Python). It allows the user to create a secured account, and get identification tokens.

## ChatGPT v.2 <a name = "chat"></a>

This little tool replacement gives you the possibility to change the model you want to use.

It allows the user to change the temperature (i.e. how the answer is given) and the maximum amount of tokens allowed.

The tool is user-friendly and presents itself as a chat with a bot

## DALL·E 2 v.2 <a name = "dalle"></a>

This tool is the same as the existing Dall-e except you can choose which resolution you want between (256*256), (512x512) and (1024x1024).

It provides the ability to download the image and save it locally.

## Notes <a name = "notes"></a>

- The output is shown in such a way that the code is displayed as code, just as the real ChatGPT application would.
- Requests can take time to be transmitted, be patient :)

