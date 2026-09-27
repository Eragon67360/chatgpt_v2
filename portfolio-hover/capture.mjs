// Captures the real ChatGPT v.2 Flet UI (served offline by app/serve.py) for the hover video.
// The viewport is the window's client area in the published screenshot (1045x684), so captures
// line up with it. Run from the repo root with the Python venv that has flet==0.9.0:
//   HOVER_KIT_DIR=<portfolio>/resources/hover-videos/kit HOVER_KIT_DEPS=<deps>/package.json \
//   PYTHON=.venv/bin/python node portfolio-hover/capture.mjs
import { spawn } from "node:child_process";
import { mkdirSync, rmSync, writeFileSync } from "node:fs";
const { openBrowser } = await import(`${process.env.HOVER_KIT_DIR}/capture.mjs`);

const here = new URL(".", import.meta.url).pathname;
const dir = `${here}captures`;
rmSync(dir, { recursive: true, force: true });
mkdirSync(dir, { recursive: true });

const server = spawn(process.env.PYTHON ?? "python", [`${here}app/serve.py`], {
  env: { ...process.env, BROWSER: "true" },
  stdio: "inherit",
});
await new Promise((r) => setTimeout(r, 6000));

const { browser, page } = await openBrowser({ width: 1045, height: 684, scale: 1.5 });
const wait = (ms) => page.waitForTimeout(ms);
const shot = (name) => page.screenshot({ path: `${dir}/${name}.jpg`, type: "jpeg", quality: 92 });
const layout = { frames: {} };

// Fixed positions in the client area (the UI is a Flutter canvas, no DOM to query).
const L = (layout.pos = { dropdown: [300, 49], optionAda: [238, 101], newChat: [40, 232], newChatLabel: [100, 232], input: [560, 649], send: [872, 648] });

/** Shoots frames while the app streams an answer; stops once two frames stay identical for 1s. */
async function record(prefix) {
  const t0 = Date.now();
  const frames = [];
  let last = null, stableSince = 0;
  for (let i = 0; Date.now() - t0 < 12000; i++) {
    const buf = await page.screenshot({ type: "jpeg", quality: 92 });
    const t = (Date.now() - t0) / 1000;
    const same = last && buf.equals(last);
    if (!same) {
      const name = `${prefix}-${String(frames.length).padStart(3, "0")}`;
      writeFileSync(`${dir}/${name}.jpg`, buf);
      frames.push([Number(t.toFixed(3)), name]);
      stableSince = t;
    } else if (t - stableSince > 1.0) break;
    last = buf;
  }
  layout.frames[prefix] = frames;
}

async function ask(text, prefix) {
  await page.mouse.click(...L.input);
  await wait(300);
  if (prefix) await shot(`${prefix}-q-0`);
  for (let i = 1; i <= text.length; i++) {
    await page.keyboard.type(text[i - 1]);
    await wait(60);
    if (prefix) await shot(`${prefix}-q-${i}`);
  }
  await page.mouse.click(...L.send);
  await page.mouse.move(700, 420);
  if (prefix) await record(`${prefix}-a`);
  else await wait(9000);
}

const Q1 = "What is ChatGPT?";
const Q2 = "Can you write me a piece of code?";
layout.q = [Q1, Q2];

await page.goto("http://127.0.0.1:8551/");
await wait(9000);
await page.mouse.click(...L.dropdown);
await wait(700);
await page.mouse.click(...L.optionAda);
await wait(1200);
await shot("model");

// The conversation of the published screenshot, then the navbar hovered and "New Chat" clicked.
await ask(Q1);
await ask(Q2);
await page.mouse.move(700, 300);
await wait(600);
await shot("full");
await page.mouse.move(...L.newChat);
await wait(900);
await shot("nav-hover");
await page.mouse.click(...L.newChatLabel);
await wait(900);
await shot("cleared");
await page.mouse.move(560, 560);
await wait(900);
await shot("empty");

// The same two questions again, recorded.
await ask(Q1, "c1");
await ask(Q2, "c2");
await page.mouse.move(700, 300);
await wait(600);
await shot("final");

writeFileSync(`${dir}/layout.js`, `window.LAYOUT = ${JSON.stringify(layout, null, 1)};\n`);
await browser.close();
server.kill();
console.log(Object.fromEntries(Object.entries(layout.frames).map(([k, v]) => [k, `${v.length} frames, ${v.at(-1)[0]}s`])));
