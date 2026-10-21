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

</div>

</div>

<div class="mt-4 px-3 py-2 rounded border border-gray-500/40 bg-gray-500/10 text-sm">
<div><b>Windows fallback</b> (PowerShell installer): <span class="font-mono text-xs whitespace-nowrap">powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"</span></div>
<div class="mt-2"><b>Last resort</b> (Python already installed): <code>python -m pip install uv</code>, then type <code>python -m uv</code> wherever the slides say <code>uv</code>.</div>
</div>

<div class="sources">
Sources: <a href="https://docs.astral.sh/uv/getting-started/installation/">docs.astral.sh/uv/getting-started/installation</a>
</div>

<!--
[Before 0:00] Students install while they arrive. Walk the room.

- Windows: winget first. Students struggled with the ExecutionPolicy installer last time, so it is only the fallback.
- winget may ask to accept source agreements: type Y. If winget is missing, App Installer from the Microsoft Store provides it.
- Why a NEW terminal: the installer changes PATH, and terminals that were already open don't see the change.
- Last resort: `python -m pip install uv` works anywhere Python exists; then `python -m uv ...` replaces `uv ...`.
- git is only needed to clone the exercises at 0:28. Download ZIP works too.
- Success = everyone sees a version number (current release: 0.13.x).
-->

---
layout: center
title: About me
---

<div class="flex items-center gap-14">

<img :src="'/somto.jpg'" alt="Somto Muotoe" onerror="this.remove()" class="w-64 h-64 rounded-full object-cover shrink-0 border-4 border-emerald-500/60" />

<div>

<div class="text-sm uppercase tracking-[0.3em] opacity-60 mb-3">About me</div>

<h1 class="!text-6xl font-bold !mb-0">Hi, I'm Somto</h1>

<div class="mt-6 text-2xl font-bold text-emerald-400">Senior ML Engineer</div>

<div class="text-xl opacity-80 mt-1">Agentic AI risk and compliance</div>

<div class="mt-8 text-lg opacity-80">In my spare time: cycling and chess</div>

</div>

</div>

<!--
[0:00-0:01] Keep it short.

- Senior ML Engineer, working on risk and compliance for agentic AI: making sure AI agents do what they should, and only that.
- That's why Part 3 matters to me: AGENTS.md, tools that check code, and verifying before you trust are the everyday version of that work.
- Outside work: cycling and chess.
-->

---
layout: default
---

# Agenda

<div class="grid grid-cols-2 gap-4 mt-6">

<div class="bg-emerald-500/10 border-l-4 border-emerald-500 px-4 py-4 rounded-r">
<div class="text-xs font-mono opacity-70">0:05 - 0:30 · Part 1</div>
<div class="font-bold text-emerald-400">uv</div>
<div class="text-sm opacity-70 mt-1">Why Python packaging was a mess, and the one tool that fixed it</div>
</div>

<div class="bg-orange-500/10 border-l-4 border-orange-500 px-4 py-4 rounded-r">
<div class="text-xs font-mono opacity-70">0:30 - 1:00 · Part 2</div>
<div class="font-bold text-orange-400">Code you can read</div>
<div class="text-sm opacity-70 mt-1">Functions, type hints, docstrings and classes. Fill in code, then review an AI's</div>
</div>

<div class="bg-pink-500/10 border-l-4 border-pink-500 px-4 py-4 rounded-r">
<div class="text-xs font-mono opacity-70">1:00 - 1:25 · Part 3</div>
<div class="font-bold text-pink-400">How code gets written today</div>
<div class="text-sm opacity-70 mt-1">Ruff, type checking, and AGENTS.md: rules your AI agent follows</div>
</div>

<div class="bg-teal-500/10 border-l-4 border-teal-500 px-4 py-4 rounded-r">
<div class="text-xs font-mono opacity-70">1:25 - 1:30</div>
<div class="font-bold text-teal-400">Wrap-up</div>
<div class="text-sm opacity-70 mt-1">Checklist, resources, questions</div>
</div>

</div>

<div class="mt-6 text-center text-sm opacity-70">
Laptops open the whole time. Setup steps, exercises and a uv cheat sheet are in the repo README.
</div>

<!--
[0:01-0:02] The plan. Three parts, each with something to do.

- Part 1 is how I set up every project now.
- Part 2 is a refresher, aimed at reading code: AI writes most of it today, but you still review it, debug it, and answer for it.
- Part 3 is how the pieces come together in real work: tools that check code automatically, and a file of rules that AI agents follow.
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
[0:02-0:05] Two quick polls. Read the options out and count hands roughly.

- Environments: note the mix. Anyone already on uv can help neighbours later.
- AI: ask who uses agents that edit files and run commands, not just chat. That sets up Part 3.
- Keep it light; this is to calibrate, not to judge.
-->
