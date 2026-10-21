---
layout: default
---

# Install uv now

<div class="text-sm opacity-70 -mt-3 mb-3">Do this while everyone settles in. It takes about a minute.</div>

<div class="grid grid-cols-2 gap-4">

<div>

<div class="text-sm font-bold text-emerald-400 mb-1">Windows (recommended)</div>

```powershell
winget install --id=astral-sh.uv -e
```

<div class="text-xs opacity-70 mt-1">Asked to accept the source agreements? Type <code>Y</code>. "winget" not recognised? Install <b>App Installer</b> from the Microsoft Store.</div>

<div class="text-sm font-bold text-emerald-400 mt-3 mb-1">macOS / Linux</div>

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

<div class="text-xs opacity-70 mt-1">Or, with Homebrew: <code>brew install uv</code></div>

</div>

<div>

<div class="text-sm font-bold text-sky-400 mb-1">Then open a NEW terminal</div>

```bash
uv --version
git --version
```

<div class="text-xs opacity-70 mt-1">No git? You can still get the exercises later: on GitHub, <b>Code &gt; Download ZIP</b>.</div>

<div class="mt-3 px-3 py-2 rounded border border-gray-500/40 bg-gray-500/10 text-xs">

**Windows fallback** (PowerShell installer):

<div class="font-mono mt-1 mb-2">powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"</div>

**Last resort** (Python already installed): `python -m pip install uv`, then type `python -m uv` wherever the slides say `uv`.

</div>

</div>

</div>

<div class="sources">
Sources: <a href="https://docs.astral.sh/uv/getting-started/installation/">docs.astral.sh/uv/getting-started/installation</a>
</div>

<!--
[0:00-0:05] Students install while you set up. Walk the room.

- Windows: winget first. Students struggled with the ExecutionPolicy installer last time, so it is only the fallback.
- winget may ask to accept source agreements: type Y. If winget is missing, App Installer from the Microsoft Store provides it.
- Why a NEW terminal: the installer changes PATH, and terminals that were already open don't see the change.
- Last resort: `python -m pip install uv` works anywhere Python exists; then `python -m uv ...` replaces `uv ...`.
- git is only needed to clone the exercises at 0:40. Download ZIP works too.
- Success = everyone sees a version number (current release: 0.13.x).
-->

---
layout: center
class: text-center
---

<div class="text-sm uppercase tracking-[0.3em] opacity-60 mb-6">About me</div>

<h1 class="!text-6xl font-bold">Hi, I'm Somto</h1>

<div class="text-2xl opacity-80 mt-6">Somto Muotoe</div>

<!--
[0:05-0:06] Add two lines about yourself.

- (line 1)
- (line 2)

This is our only session before the course starts in January.
-->

---
layout: default
---

# Agenda

<div class="grid grid-cols-3 gap-3 mt-4">

<div class="bg-blue-500/10 border-l-4 border-blue-500 px-3 py-2 rounded-r">
<div class="text-xs font-mono opacity-70">0:00 - 0:10</div>
<div class="font-bold text-blue-400">Install + intro</div>
<div class="text-sm opacity-70 mt-1">uv on every laptop, who is in the room</div>
</div>

<div class="bg-purple-500/10 border-l-4 border-purple-500 px-3 py-2 rounded-r">
<div class="text-xs font-mono opacity-70">0:10 - 0:15</div>
<div class="font-bold text-purple-400">How things have shifted</div>
<div class="text-sm opacity-70 mt-1">Python packaging and AI coding, then and now</div>
</div>

<div class="bg-emerald-500/10 border-l-4 border-emerald-500 px-3 py-2 rounded-r">
<div class="text-xs font-mono opacity-70">0:15 - 0:40</div>
<div class="font-bold text-emerald-400">uv</div>
<div class="text-sm opacity-70 mt-1">Projects, dependencies, Python versions, scripts, tools</div>
</div>

<div class="bg-orange-500/10 border-l-4 border-orange-500 px-3 py-2 rounded-r">
<div class="text-xs font-mono opacity-70">0:40 - 1:15</div>
<div class="font-bold text-orange-400">Functions, docstrings, classes</div>
<div class="text-sm opacity-70 mt-1">Hands-on: three exercises</div>
</div>

<div class="bg-pink-500/10 border-l-4 border-pink-500 px-3 py-2 rounded-r">
<div class="text-xs font-mono opacity-70">1:15 - 1:27</div>
<div class="font-bold text-pink-400">Coding with AI</div>
<div class="text-sm opacity-70 mt-1">Specify, generate, verify, explain</div>
</div>

<div class="bg-teal-500/10 border-l-4 border-teal-500 px-3 py-2 rounded-r">
<div class="text-xs font-mono opacity-70">1:27 - 1:30</div>
<div class="font-bold text-teal-400">Wrap-up</div>
<div class="text-sm opacity-70 mt-1">Checklist, resources, questions</div>
</div>

</div>

<div class="mt-6 text-center text-sm opacity-70">
Laptops open the whole time. Everything we run today is in the repo README.
</div>

<!--
[0:06-0:07] The plan. Half of today is hands-on.

- The uv block is the part I care about most: it is how I set up every project.
- The fundamentals block is a refresher, but with today's habits: type hints, docstrings, small functions.
- The AI block ties it together: the same habits make AI output better and easier to check.
-->

---
layout: default
---

# Quick poll: show of hands

<div class="grid grid-cols-2 gap-6 mt-6">

<div class="px-4 py-3 rounded border border-blue-500/30 bg-blue-500/5">
<div class="text-lg font-bold text-blue-400 mb-3">How do you manage Python environments today?</div>
<div class="flex flex-wrap gap-2 text-sm">
<span class="px-3 py-1 rounded-full border border-blue-400/50">pip + venv</span>
<span class="px-3 py-1 rounded-full border border-blue-400/50">conda</span>
<span class="px-3 py-1 rounded-full border border-blue-400/50">poetry</span>
<span class="px-3 py-1 rounded-full border border-blue-400/50">uv</span>
<span class="px-3 py-1 rounded-full border border-blue-400/50">whatever works</span>
</div>
</div>

<div class="px-4 py-3 rounded border border-pink-500/30 bg-pink-500/5">
<div class="text-lg font-bold text-pink-400 mb-3">Do you use AI to write code?</div>
<div class="flex flex-wrap gap-2 text-sm">
<span class="px-3 py-1 rounded-full border border-pink-400/50">chat (ChatGPT, Claude, ...)</span>
<span class="px-3 py-1 rounded-full border border-pink-400/50">autocomplete (Copilot, ...)</span>
<span class="px-3 py-1 rounded-full border border-pink-400/50">agents (Claude Code, Codex, ...)</span>
<span class="px-3 py-1 rounded-full border border-pink-400/50">not yet</span>
</div>
</div>

</div>

<div class="mt-8 text-center text-sm opacity-70">
No wrong answers. "Whatever works" is the most honest one.
</div>

<!--
[0:07-0:10] Two quick polls. Read the options out and count hands roughly.

- Environments: expect mostly pip + venv and conda. Anyone already on uv can help neighbours later.
- AI: ask who uses agents that edit files and run commands, not just chat. That sets up the next section.
- Keep it light; this is to calibrate, not to judge.
-->
