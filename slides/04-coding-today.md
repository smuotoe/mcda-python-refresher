---
layout: center
class: text-center
title: "Part 3: How code gets written today"
---

<div class="absolute inset-0" style="background: radial-gradient(circle at 50% 45%, rgba(236, 72, 153, 0.18), transparent 60%);"></div>

<div class="relative z-10">

<div class="text-sm uppercase tracking-[0.3em] text-pink-400 mb-4">Part 3 · 1:00 - 1:25</div>

<h1 class="!text-6xl font-bold">How code gets written today</h1>

<div class="text-xl opacity-80 mt-6">Tools that check your code, and rules your AI agent follows</div>

</div>

<!--
[1:00] Section transition. Part 2 was you reading code. Part 3 is how you get tools and agents to do most of the checking and writing, the way teams actually work.
-->

---
layout: default
---

# A project, the way teams set one up

<div class="grid grid-cols-2 gap-5 mt-1">

<div>

```text
my-app/
├── AGENTS.md        rules for AI coding agents
├── README.md        how to set up and run it
├── pyproject.toml   dependencies + tool settings
├── uv.lock          exact versions
├── .python-version
├── .env             secrets: never shared
└── main.py
```

```toml
# pyproject.toml
[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "D"]

[tool.ruff.lint.pydocstyle]
convention = "google"
```

</div>

<div class="space-y-2 text-sm">

<div class="px-3 py-2 rounded border border-emerald-500/30 bg-emerald-500/5">
<div class="font-bold text-emerald-400">uv: environment and dependencies</div>
<div>Part 1.</div>
</div>

<div class="px-3 py-2 rounded border border-pink-500/30 bg-pink-500/5">
<div class="font-bold text-pink-400">Ruff: lint and format</div>
<div>Finds bug patterns, unused imports and missing docstrings, and formats everything the same way. <code>uvx ruff check .</code> · <code>uvx ruff format .</code></div>
</div>

<div class="px-3 py-2 rounded border border-sky-500/30 bg-sky-500/5">
<div class="font-bold text-sky-400">A type checker</div>
<div>Checks that the type hints agree with the code. In VS Code it's the red squiggles. On the command line: <code>uvx ty check</code> (beta).</div>
</div>

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400">AGENTS.md: rules for your agent</div>
<div>Plain Markdown. Coding agents read it before they start: Codex, Cursor, GitHub Copilot, Claude Code and more (a few need a setting).</div>
</div>

</div>

</div>

<div class="sources">
Sources: <a href="https://docs.astral.sh/ruff/">docs.astral.sh/ruff</a> · <a href="https://docs.astral.sh/ty/">docs.astral.sh/ty</a> · <a href="https://agents.md/">agents.md</a>
</div>

<!--
[1:00-1:03] The kit. Every item is something a real team has in its repo.

- Ruff and ty are both by Astral (the uv people), and both run through uvx with nothing to install.
- The ruff config shown is the one in this repo's pyproject.toml: defaults (E, F) plus import sorting (I), common bug patterns (B), modern syntax (UP), and docstrings (D, Google convention).
- ty is Astral's type checker; it is still pre-1.0 (0.0.x in Oct 2026). Pyright/Pylance (what VS Code uses) and mypy are the established alternatives.
- AGENTS.md: released by OpenAI in Aug 2025, now stewarded by the Linux Foundation's Agentic AI Foundation. agents.md lists Codex, Cursor, GitHub Copilot's coding agent, Jules, VS Code and many more; Gemini CLI and Aider need a setting. Claude Code reads it too (v2.1.277+) when there is no CLAUDE.md.
-->

---
layout: default
---

# Demo: let the tools review first

<div class="text-sm opacity-70 -mt-3 mb-3">On the original <code>exercises/review.py</code>, before any fixes</div>

<div class="grid grid-cols-2 gap-5">

<div>

```bash
uvx ruff check exercises/review.py
uvx ty check exercises/review.py
uvx ruff format --diff exercises/review.py
```

<div class="mt-3 px-3 py-2 rounded border-l-4 border-pink-500 bg-pink-500/10 text-sm">
Seconds to run, nothing to install, and they never get tired. Your agent can run them too, if you tell it to.
</div>

</div>

<div>

<table class="w-full text-sm border border-gray-600">
<thead>
<tr class="border-b-2 border-pink-500 bg-pink-500/20">
<th class="text-left py-1 px-2 border-r border-gray-600">Bug from Exercise 2</th>
<th class="text-left py-1 px-2">Caught by</th>
</tr>
</thead>
<tbody>
<tr class="border-b border-gray-600"><td class="py-1 px-2 border-r border-gray-600">strings instead of floats</td><td class="py-1 px-2">type checker</td></tr>
<tr class="border-b border-gray-600"><td class="py-1 px-2 border-r border-gray-600">mutable default argument</td><td class="py-1 px-2">Ruff (<code>B006</code>)</td></tr>
<tr><td class="py-1 px-2 border-r border-gray-600"><code>ranked[: n - 1]</code></td><td class="py-1 px-2 font-bold text-orange-400">only you</td></tr>
</tbody>
</table>

<div class="mt-4 text-center text-lg font-bold">
Tools catch the patterns.<br/>You catch the logic.
</div>

</div>

</div>

<div class="sources">
Sources: <a href="https://docs.astral.sh/ruff/rules/mutable-argument-default/">Ruff rule B006</a> · <a href="https://docs.astral.sh/ty/">docs.astral.sh/ty</a>
</div>

<!--
[1:03-1:07] Run the three commands live, on your UNFIXED copy of review.py.

- `uvx ruff check`: reports B006 (mutable argument default) on add_comment.
- `uvx ty check`: reports invalid-return-type on parse_scores: expected list[float], found a list containing str.
- `uvx ruff format --diff`: shows what formatting would change (probably nothing here; that's the point of a formatter: no debates about style).
- The off-by-one is invisible to both: the code is perfectly valid, it just doesn't do what the docstring says. That's what reading, or a test with a known answer, is for.
-->

---
layout: default
---

# Demo: with and without AGENTS.md

<div class="grid grid-cols-5 gap-4 mt-1">

<div class="col-span-2">

<div class="text-sm font-bold text-pink-400 mb-1">The prompt, both times</div>

<div class="px-3 py-2 rounded bg-gray-500/10 text-sm italic">"Read scores.csv and print each student's average score and letter grade."</div>

<div class="text-sm font-bold text-pink-400 mt-3 mb-1">From <code>starter/AGENTS.md</code></div>

```markdown
- Use uv for everything: `uv add` to add
  a dependency, `uv run` to run code.
  Never call pip.
- Type hints and a Google-style
  docstring on every function.
- Run `uvx ruff check .` and fix what
  it reports. Run the code.
```

</div>

<div class="col-span-3">

<div class="text-sm font-bold mb-1">Watch for</div>

<table class="w-full text-sm border border-gray-600">
<thead>
<tr class="border-b-2 border-pink-500 bg-pink-500/20">
<th class="text-left py-1 px-2 border-r border-gray-600"></th>
<th class="text-left py-1 px-2 border-r border-gray-600">Without</th>
<th class="text-left py-1 px-2">With</th>
</tr>
</thead>
<tbody>
<tr class="border-b border-gray-600"><td class="py-1 px-2 border-r border-gray-600">installs packages with</td><td class="py-1 px-2 border-r border-gray-600 opacity-70">?</td><td class="py-1 px-2 opacity-70">?</td></tr>
<tr class="border-b border-gray-600"><td class="py-1 px-2 border-r border-gray-600">type hints and docstrings</td><td class="py-1 px-2 border-r border-gray-600 opacity-70">?</td><td class="py-1 px-2 opacity-70">?</td></tr>
<tr class="border-b border-gray-600"><td class="py-1 px-2 border-r border-gray-600">runs Ruff</td><td class="py-1 px-2 border-r border-gray-600 opacity-70">?</td><td class="py-1 px-2 opacity-70">?</td></tr>
<tr><td class="py-1 px-2 border-r border-gray-600">runs the code and shows output</td><td class="py-1 px-2 border-r border-gray-600 opacity-70">?</td><td class="py-1 px-2 opacity-70">?</td></tr>
</tbody>
</table>

<div class="mt-4 px-3 py-2 rounded border-l-4 border-pink-500 bg-pink-500/10 text-sm">
Without AGENTS.md you get the agent's habits. With it you get <b>yours</b>, every time, without repeating yourself in every prompt.
</div>

</div>

</div>

<!--
[1:07-1:13] Live demo with whichever agent you use. Fill in the table out loud as the room watches.

Setup (before class, in a scratch folder):
  uv init --no-package without-rules
  uv init --no-package with-rules
  copy starter/scores.csv into both; copy starter/AGENTS.md into with-rules only

Then:
1. Open the agent in without-rules, give it the prompt. Narrate: what did it install, and how? (pip install pandas is common.) Hints? Docstrings? Did it run anything?
2. Same prompt in with-rules. Narrate the differences: `uv add`, hints and docstrings, a ruff run, output shown.
3. Open the with-rules main.py and point at a docstring: "I didn't write that. I required it."

Results vary between agents and runs. Rehearse with your agent and keep a screen recording as a backup. If the agent behaves well even without the file, that's still the point: without AGENTS.md you're relying on its defaults; with it, your rules are written down and the same for everyone.

Make sure the CSV has no secrets and the agent works in a throwaway folder.
-->

---
layout: default
---

# Exercise 3: your own AGENTS.md, in pairs (8 min)

<div class="grid grid-cols-2 gap-5 mt-1">

<div>

<div class="text-sm opacity-80 mb-1">Next to the repo folder, not inside it:</div>

```bash
uv init --no-package grades
cd grades
cp ../mcda-python-refresher/starter/* .
```

<div class="text-xs opacity-70 mt-1"><code>cp</code> works in PowerShell too.</div>

<div class="mt-3 space-y-2 text-sm">
<div class="px-3 py-2 rounded border-l-4 border-pink-500 bg-pink-500/10"><b>1.</b> Add one rule of your own to <code>AGENTS.md</code>, e.g. "print results as a rich table" or "explain your changes in plain English".</div>
<div class="px-3 py-2 rounded border-l-4 border-pink-500 bg-pink-500/10"><b>2.</b> Give your agent the prompt from the demo.</div>
<div class="px-3 py-2 rounded border-l-4 border-pink-500 bg-pink-500/10"><b>3.</b> Check its work, below.</div>
</div>

</div>

<div>

<div class="px-3 py-2 rounded border border-pink-500/30 bg-pink-500/5 text-sm">
<div class="font-bold text-pink-400 mb-1">Did it follow every rule?</div>
<div class="space-y-1">
<div><code>uv run main.py</code>: does it run? Ada's average is 91.67, an A</div>
<div><code>uvx ruff check .</code>: clean?</div>
<div><code>pyproject.toml</code>: any new dependencies? Did it ask first?</div>
<div>Your own rule: followed?</div>
<div>Could you explain every line to your partner?</div>
</div>
</div>

<div class="mt-3 px-3 py-2 rounded bg-gray-500/10 text-sm">
<div><b>Agent in your editor</b> (Copilot, Cursor, Claude Code, Codex, ...): it reads AGENTS.md itself.</div>
<div class="mt-1"><b>Chat only</b> (ChatGPT, Claude, Gemini): paste AGENTS.md and the prompt; you run the commands.</div>
<div class="mt-1"><b>No AI access:</b> pair with someone who has it.</div>
</div>

</div>

</div>

<!--
[1:13-1:21] Pairs. One laptop with an agent per pair is enough.

- The copy line: works in bash/zsh and in PowerShell (cp is an alias for Copy-Item, and PowerShell accepts forward slashes). Students who used Download ZIP may have a folder called mcda-python-refresher-main; adjust the path.
- Ada's scores in scores.csv are 92, 88, 95: mean 91.67, an A. Use it as the known answer.
- Ask a few pairs: what rule did you add, and did the agent follow it?
- GitHub Copilot is free for verified students; mention it for anyone without access.
-->

---
layout: default
---

# Verify before you trust

<div class="grid grid-cols-2 gap-4 mt-1">

<div class="px-3 py-2 rounded border border-emerald-500/30 bg-emerald-500/5">
<div class="font-bold text-emerald-400 mb-1">Run it against answers you know</div>
<div class="text-sm">Pick inputs where you already know the output, like Ada's 91.67. "It ran" is not "it's right."</div>
</div>

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400 mb-1">Read it</div>
<div class="text-sm">Let Ruff and the type checker go first, then read what's left. If you can't explain a line, ask the agent to, or rewrite it.</div>
</div>

<div class="px-3 py-2 rounded border border-pink-500/30 bg-pink-500/5">
<div class="font-bold text-pink-400 mb-1">Check new packages exist</div>
<div class="text-sm">AIs sometimes invent package names, and attackers register them ("slopsquatting"). One study found made-up packages in 5.2% to 21.7% of AI code samples. Look it up on pypi.org before <code>uv add</code>: its age, downloads, and linked repo.</div>
</div>

<div class="px-3 py-2 rounded border border-sky-500/30 bg-sky-500/5">
<div class="font-bold text-sky-400 mb-1">Keep secrets and private data out</div>
<div class="text-sm">API keys go in <code>.env</code>, read from environment variables. Don't paste private data or credentials into public chat tools.</div>
</div>

</div>

<div class="sources">
Sources: Spracklen et al., <a href="https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen">"We Have a Package for You!", USENIX Security 2025</a> (<a href="https://arxiv.org/abs/2406.10279">arXiv 2406.10279</a>)
</div>

<!--
[1:21-1:25] Four habits for anything an agent writes.

- Known answers: the cheapest test there is. Exercise 2's expected comments were exactly this.
- Read it: the tools cleared two of three bugs in the demo; the third needed a human.
- Package hallucination: the paper tested 16 models on 576,000 generated code samples; hallucinated packages appeared in at least 5.2% (commercial models) and 21.7% (open-source models) of cases, 205,474 unique fake names. "Slopsquatting" is credited to Seth Larson (PSF). Show pypi.org/project/requests next to a search for a made-up name: no page means do not install.
- Secrets: .env plus .gitignore; the starter AGENTS.md already tells the agent to read secrets from environment variables. Public chat tools may keep what you paste; use the tools your employer or school approves for private code.
-->
