"""
Interface for chatGPT
"""
import view
from flet import *
from view import ChangeRoute

text_home = [
        "\"Explain quantum computing in simple terms\"",
        "Remembers what user said earlier in the conversation",
        "May occasionally generate incorrect information",
        "\"Got any creative ideas for a 10 year Old's birthday?\"",
        "Allows user to provide follow-up corrections",
        "May occasionally produce harmful instructions or biased content",
        "\"How do I make an HTTP request in Javascript?\"",
        "Trained to decline inappropriate requests",
        "Limited knowledge of world and events after 2021"
]


class GPT(UserControl):
    def __init__(self):
        self.list_questions = []
        self.list_answers = []

        self.model_davinci = "text-davinci-003"
        super().__init__()

    def build(self):
        return Container(
            Text("TEST")

        )