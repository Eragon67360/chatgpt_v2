# portfolio-hover

Source of the hover preview shown on thomasmoserdev.com/projects for this project.

- `app/serve.py`: serves the real Flet UI from `ChatGPT/` as a web app, fully offline. The code in
  `ChatGPT/` is untouched; only its network boundaries are stubbed in-process (empty `API` keys, an inert
  `pyrebase`, and a `gpt_control` that replays the two answers visible in the project's published
  screenshot). No OpenAI or Firebase request is made, no key is needed. Needs `flet==0.9.0` and `urllib3`
  (the app predates Flet 1.0), e.g. `uv venv --python 3.11 .venv && uv pip install flet==0.9.0 urllib3`.
- `capture.mjs`: starts the server, drives the UI with Playwright at the window's client size in the
  screenshot (1045x684, 1.5x density) and saves the states into `captures/`: model picked, navbar hovered,
  "New Chat", both questions typed character by character, and the answers streamed by the app's own code.
- `comp.html`: the 8s, 1280x800 loop. It starts and ends on the card screenshot (`captures/card.png`,
  shown like the card: scaled to the width, top-aligned) and plays the captures in between.
- `out/`: rendered `openai-clone.mp4` (silent H.264) and its first frame.

`engine.js`, `base.css` and `render.mjs` are copied from the portfolio's `resources/hover-videos/kit`,
which documents how to capture and render.
