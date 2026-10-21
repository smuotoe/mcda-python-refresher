---
layout: default
---

# Python packaging: one problem at a time

<div class="text-sm opacity-70 -mt-3 mb-3">Every few years a new tool fixed one piece. uv is the first to cover all of them.</div>

<div class="grid grid-cols-4 gap-2 text-sm">

<div class="px-2 py-1 rounded border-l-4 border-blue-500 bg-blue-500/10">
<div class="font-mono text-xs text-blue-400">2007</div>
<div class="font-bold">virtualenv</div>
<div class="text-xs opacity-70">isolated environments</div>
</div>

<div class="px-2 py-1 rounded border-l-4 border-blue-500 bg-blue-500/10">
<div class="font-mono text-xs text-blue-400">2008</div>
<div class="font-bold">pip</div>
<div class="text-xs opacity-70">the package installer</div>
</div>

<div class="px-2 py-1 rounded border-l-4 border-blue-500 bg-blue-500/10">
<div class="font-mono text-xs text-blue-400">2012</div>
<div class="font-bold">venv in the standard library</div>
<div class="text-xs opacity-70">Python 3.3, PEP 405</div>
</div>

<div class="px-2 py-1 rounded border-l-4 border-blue-500 bg-blue-500/10">
<div class="font-mono text-xs text-blue-400">2012</div>
<div class="font-bold">conda</div>
<div class="text-xs opacity-70">packages beyond Python</div>
</div>

<div class="px-2 py-1 rounded border-l-4 border-purple-500 bg-purple-500/10">
<div class="font-mono text-xs text-purple-400">2016</div>
<div class="font-bold">pyproject.toml</div>
<div class="text-xs opacity-70">PEP 518: build requirements</div>
</div>

<div class="px-2 py-1 rounded border-l-4 border-purple-500 bg-purple-500/10">
<div class="font-mono text-xs text-purple-400">2017</div>
<div class="font-bold">Pipenv</div>
<div class="text-xs opacity-70">Pipfile + lock file</div>
</div>

<div class="px-2 py-1 rounded border-l-4 border-purple-500 bg-purple-500/10">
<div class="font-mono text-xs text-purple-400">2018</div>
<div class="font-bold">Poetry</div>
<div class="text-xs opacity-70">dependencies, lock, build</div>
</div>

<div class="px-2 py-1 rounded border-l-4 border-purple-500 bg-purple-500/10">
<div class="font-mono text-xs text-purple-400">2020</div>
<div class="font-bold">PEP 621</div>
<div class="text-xs opacity-70">project metadata in pyproject.toml</div>
</div>

<div class="px-2 py-1 rounded border-l-4 border-emerald-500 bg-emerald-500/10">
<div class="font-mono text-xs text-emerald-400">Feb 2024</div>
<div class="font-bold">uv</div>
<div class="text-xs opacity-70">a fast pip replacement</div>
</div>

<div class="px-2 py-1 rounded border-l-4 border-emerald-500 bg-emerald-500/10">
<div class="font-mono text-xs text-emerald-400">2024</div>
<div class="font-bold">PEP 723</div>
<div class="text-xs opacity-70">inline script metadata (accepted)</div>
</div>

<div class="px-2 py-1 rounded border-l-4 border-emerald-500 bg-emerald-500/10">
<div class="font-mono text-xs text-emerald-400">Aug 2024</div>
<div class="font-bold">uv, full project manager</div>
<div class="text-xs opacity-70">projects, lock files, Python versions, tools</div>
</div>

<div class="px-2 py-1 rounded border-l-4 border-emerald-500 bg-emerald-500/10">
<div class="font-mono text-xs text-emerald-400">2025</div>
<div class="font-bold">PEP 751</div>
<div class="text-xs opacity-70">a standard lock file format (accepted)</div>
</div>

</div>

<div class="sources">
Sources: PyPI release histories for <a href="https://pypi.org/project/virtualenv/#history">virtualenv</a>, <a href="https://pypi.org/project/pip/#history">pip</a>, <a href="https://pypi.org/project/pipenv/#history">Pipenv</a>, <a href="https://pypi.org/project/poetry/#history">Poetry</a> ·
<a href="https://peps.python.org/pep-0405/">PEP 405</a> · <a href="https://www.python.org/downloads/release/python-330/">Python 3.3.0</a> · <a href="https://docs.conda.io/projects/conda/en/latest/release-notes.html">conda release notes</a> ·
<a href="https://peps.python.org/pep-0518/">PEP 518</a> · <a href="https://peps.python.org/pep-0621/">PEP 621</a> · <a href="https://peps.python.org/pep-0723/">PEP 723</a> · <a href="https://peps.python.org/pep-0751/">PEP 751</a> ·
<a href="https://astral.sh/blog/uv">astral.sh/blog/uv</a> · <a href="https://astral.sh/blog/uv-unified-python-packaging">astral.sh/blog/uv-unified-python-packaging</a>
</div>

<!--
[0:10-0:12] The story, left to right, top to bottom:

- Environments came first (virtualenv, then venv in the standard library).
- pip became the default installer. conda solved non-Python dependencies (C libraries, CUDA) for science.
- pyproject.toml gave projects one config file; Pipenv and Poetry added lock files.
- PEP 621 standardised project metadata, so tools could agree on [project].
- uv started as a fast pip replacement (Feb 2024) and became a full project manager (Aug 2024).
- PEP 723 standardised single-file scripts with dependencies; PEP 751 standardised a lock file format.

Point: each tool fixed one problem, so you ended up juggling five tools. That is what uv replaces.
-->

---
layout: default
---

# AI and coding: autocomplete, then chat, then agents

<div class="grid grid-cols-3 gap-3 mt-4">

<div class="px-3 py-2 rounded border border-sky-500/30 bg-sky-500/5">
<div class="text-xs uppercase tracking-widest text-sky-400">Autocomplete</div>
<div class="text-sm opacity-70 mb-2">AI finishes the line you are typing</div>
<div class="text-sm"><span class="font-mono text-xs text-sky-400">Jun 2021</span><br/>GitHub Copilot technical preview</div>
</div>

<div class="px-3 py-2 rounded border border-purple-500/30 bg-purple-500/5">
<div class="text-xs uppercase tracking-widest text-purple-400">Chat</div>
<div class="text-sm opacity-70 mb-2">You ask, you copy, you paste</div>
<div class="text-sm space-y-2">
<div><span class="font-mono text-xs text-purple-400">Nov 2022</span><br/>ChatGPT</div>
<div><span class="font-mono text-xs text-purple-400">Mar 2023</span><br/>GPT-4</div>
</div>
</div>

<div class="px-3 py-2 rounded border border-pink-500/30 bg-pink-500/5">
<div class="text-xs uppercase tracking-widest text-pink-400">Agents</div>
<div class="text-sm opacity-70 mb-2">AI edits files and runs commands in your terminal</div>
<div class="text-sm space-y-1">
<div><span class="font-mono text-xs text-pink-400">Feb 2025</span> "vibe coding" (Karpathy)</div>
<div><span class="font-mono text-xs text-pink-400">Feb 2025</span> Claude Code preview (GA May 2025)</div>
<div><span class="font-mono text-xs text-pink-400">Apr 2025</span> OpenAI Codex CLI</div>
<div><span class="font-mono text-xs text-pink-400">Jun 2025</span> Gemini CLI</div>
<div><span class="font-mono text-xs text-pink-400">Aug 2025</span> AGENTS.md rules files</div>
</div>
</div>

</div>

<div class="mt-5 text-center text-sm opacity-80">
Each step hands the AI more of the work, and leaves you more to check.
</div>

<div class="sources">
Sources: <a href="https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/">GitHub blog (Copilot)</a> · <a href="https://openai.com/index/chatgpt/">OpenAI (ChatGPT)</a> · <a href="https://openai.com/index/gpt-4-research/">OpenAI (GPT-4)</a> · <a href="https://x.com/karpathy/status/1886192184808149383">Karpathy on X</a> ·
<a href="https://www.anthropic.com/news/claude-3-7-sonnet">Anthropic (Feb 2025)</a> · <a href="https://www.anthropic.com/news/claude-4">Anthropic (May 2025)</a> · <a href="https://openai.com/index/introducing-o3-and-o4-mini/">OpenAI (Codex CLI)</a> · <a href="https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/">Google (Gemini CLI)</a> · <a href="https://agents.md/">agents.md</a>
</div>

<!--
[0:12-0:13:30] Three eras in four years.

- Autocomplete: Copilot predicted the next line inside your editor.
- Chat: ChatGPT and GPT-4 made "ask for a whole function" normal. You still copied and pasted.
- Agents: tools like Claude Code, Codex CLI and Gemini CLI read your repo, edit files, and run commands.
- "Vibe coding": Karpathy's name for accepting AI code without reading it. Fun for throwaway projects, risky for anything you have to maintain.
- AGENTS.md: a plain Markdown file of project rules that agents read. Our repo has one; we will look at it later.
-->

---
layout: default
---

# What this changes for you

<div class="grid grid-cols-5 gap-4 mt-2">

<div class="col-span-2">

<div class="px-3 py-2 rounded border-l-4 border-gray-400 bg-gray-500/10 text-sm">
<div class="text-xs uppercase tracking-widest opacity-60 mb-1">My course plan, 2023</div>
"...the bulk of the code can be written by GPT-4 or other coding assistants"
</div>

<div class="px-3 py-2 mt-2 rounded border-l-4 border-pink-500 bg-pink-500/10 text-sm">
<div class="text-xs uppercase tracking-widest text-pink-400 mb-1">2026</div>
Agents write whole features, across many files.
</div>

<div class="mt-3 text-sm font-bold">Typing code is cheap now. The scarce skills:</div>

</div>

<div class="col-span-3 grid grid-cols-3 gap-2 content-start">

<div class="px-2 py-2 rounded border border-sky-500/30 bg-sky-500/5">
<div class="font-bold text-sky-400">Specify</div>
<div class="text-xs opacity-70">say exactly what you want</div>
</div>

<div class="px-2 py-2 rounded border border-emerald-500/30 bg-emerald-500/5">
<div class="font-bold text-emerald-400">Verify</div>
<div class="text-xs opacity-70">check what you got</div>
</div>

<div class="px-2 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400">Explain</div>
<div class="text-xs opacity-70">defend every line</div>
</div>

<div class="col-span-3 mt-1 px-3 py-2 rounded bg-gray-500/10 text-sm">
Type hints and docstrings are how you talk to <b>both</b> the humans and the AI that read your code.
</div>

<div class="col-span-3 grid grid-cols-2 gap-2 mt-1">
<div class="px-3 py-2 rounded border border-gray-500/30 text-xs">
<div class="text-2xl font-bold text-pink-400">84%</div>
of developers use or plan to use AI tools; more distrust their accuracy (46%) than trust it (33%).
<div class="opacity-60 mt-1">Stack Overflow Developer Survey 2025</div>
</div>
<div class="px-3 py-2 rounded border border-gray-500/30 text-xs">
<div class="text-2xl font-bold text-orange-400">19% slower</div>
Experienced open-source developers using AI took longer, yet believed AI had sped them up.
<div class="opacity-60 mt-1">METR randomized trial, July 2025</div>
</div>
</div>

</div>

</div>

<div class="sources">
Sources: <a href="https://survey.stackoverflow.co/2025/ai">survey.stackoverflow.co/2025/ai</a> · <a href="https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/">metr.org (July 2025 study)</a>
</div>

<!--
[0:13:30-0:15] One slide, one message.

- In 2023 my course plan already said GPT-4 could write the bulk of the code. Three years later, agents write whole features.
- So typing is no longer the bottleneck. Specifying, verifying and explaining are.
- Type hints and docstrings are the cheapest way to specify. They help your teammates, your future self, and the AI.
- Stack Overflow 2025: nearly everyone uses AI, but trust is low. That is healthy.
- METR: in a randomized trial, experienced developers on their own repos were 19% slower with AI, while believing they were faster. Feeling productive is not the same as being productive; measure and verify.
-->
