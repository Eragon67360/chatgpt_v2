"""Serves the real ChatGPT v.2 Flet UI as a web app, offline, for the portfolio hover capture.

Nothing in ChatGPT/ is modified. Only the network boundaries are replaced in-process:
- `API` (the git-ignored key file) gets empty keys,
- `pyrebase` (Firebase login) gets an inert stub; the harness opens the chat page directly,
- `gpt_control` (OpenAI calls) returns a fixed model list and replays the answers that are
  visible in the project's published screenshot, so no request ever leaves the machine.

Run: .venv/bin/python portfolio-hover/app/serve.py  (serves http://127.0.0.1:8551)
Requires flet==0.9.0 (the app uses UserControl and the pre-1.0 API).
"""
import os
import sys
import time
import types

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ChatGPT")
os.chdir(ROOT)
sys.path.insert(0, ROOT)

sys.modules["API"] = types.SimpleNamespace(API_KEY="", API_FIREBASE="")


class _Inert:
    def __getattr__(self, name):
        return lambda *a, **k: _Inert()


sys.modules["pyrebase"] = types.SimpleNamespace(initialize_app=lambda cfg: _Inert())

# Answers shown in the published screenshot of the app (assets on thomasmoserdev.com).
ANSWERS = {
    "What is ChatGPT?": (
        "ChatGPT is an open-source natural language processing (NLP) model that enables developers "
        "to create conversational AI applications. It is based on the GPT-3 model, which is a "
        "transformer-based language model that uses deep learning to generate human-like text. "
        "ChatGPT can be used to create chatbots, virtual assistants, and other conversational AI "
        "applications."
    ),
    "Can you write me a piece of code?": (
        '```\n#include <stdio.h>\n\nint main()\n{\n    printf("Hello World!");\n    return 0;\n}\n```'
    ),
}
gpt_control = types.ModuleType("gpt_control")
gpt_control.getModelIDs = lambda: ["text-davinci-003", "text-embedding-ada-002", "code-davinci-002"]


def _completion(model, prompt, **kwargs):
    time.sleep(0.6)  # stands in for the network round trip
    return ANSWERS.get(prompt.replace("(generate your answer using markdown)", ""), "")


gpt_control.getCompletion = _completion
sys.modules["gpt_control"] = gpt_control

import flet as ft  # noqa: E402
import main as app_main  # noqa: E402  (builds the page registry from ./pages)


def target(page: ft.Page):
    # Same setup as ChatGPT/main.py, then the chat page instead of the Firebase login.
    page.title = "OpenAI All-In-One"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    page.dark_theme = ft.Theme(page_transitions=ft.PageTransitionsTheme.ios)
    page.overlay.clear()
    page.overlay.append(
        ft.Column(
            opacity=0.1,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[ft.Text("", size=30)])],
        )
    )
    page.views.clear()
    page.views.append(app_main._moduleList["/chatgpt"].loader.load_module()._view_(page))
    page.go("/chatgpt")
    page.update()


ft.app(target=target, view=ft.WEB_BROWSER, port=8551)
