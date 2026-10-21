---
layout: default
---

# Python packaging: one problem at a time

<div class="text-sm opacity-70 -mt-3 mb-3">Every few years a new tool fixed one piece. uv now covers all of them in one tool.</div>

<div class="grid grid-cols-4 gap-3">

<div class="px-3 py-2 rounded border-l-4 border-blue-500 bg-blue-500/10">
<div class="font-mono text-xs text-blue-400">Sep 2007</div>
<div class="font-bold">virtualenv</div>
<div class="text-xs opacity-70">isolated environments</div>
</div>

<div class="px-3 py-2 rounded border-l-4 border-blue-500 bg-blue-500/10">
<div class="font-mono text-xs text-blue-400">Oct 2008</div>
<div class="font-bold">pip</div>
<div class="text-xs opacity-70">the package installer</div>
</div>

<div class="px-3 py-2 rounded border-l-4 border-blue-500 bg-blue-500/10">
<div class="font-mono text-xs text-blue-400">Sep 2012</div>
<div class="font-bold">venv in the standard library</div>
<div class="text-xs opacity-70">Python 3.3, PEP 405</div>
</div>

<div class="px-3 py-2 rounded border-l-4 border-blue-500 bg-blue-500/10">
<div class="font-mono text-xs text-blue-400">Sep 2012</div>
<div class="font-bold">conda</div>
<div class="text-xs opacity-70">packages beyond Python</div>
</div>

<div class="px-3 py-2 rounded border-l-4 border-purple-500 bg-purple-500/10">
<div class="font-mono text-xs text-purple-400">May 2016</div>
<div class="font-bold">pyproject.toml</div>
<div class="text-xs opacity-70">PEP 518: one config file</div>
</div>

<div class="px-3 py-2 rounded border-l-4 border-purple-500 bg-purple-500/10">
<div class="font-mono text-xs text-purple-400">Jan 2017</div>
<div class="font-bold">Pipenv</div>
<div class="text-xs opacity-70">Pipfile + lock file</div>
</div>

<div class="px-3 py-2 rounded border-l-4 border-purple-500 bg-purple-500/10">
<div class="font-mono text-xs text-purple-400">Feb 2018</div>
<div class="font-bold">Poetry</div>
<div class="text-xs opacity-70">dependencies, lock, build</div>
</div>

<div class="px-3 py-2 rounded border-l-4 border-purple-500 bg-purple-500/10">
<div class="font-mono text-xs text-purple-400">Nov 2020</div>
<div class="font-bold">PEP 621</div>
<div class="text-xs opacity-70">project metadata in pyproject.toml</div>
</div>

<div class="px-3 py-2 rounded border-l-4 border-emerald-500 bg-emerald-500/10">
<div class="font-mono text-xs text-emerald-400">Jan 2024</div>
<div class="font-bold">PEP 723</div>
<div class="text-xs opacity-70">inline script metadata</div>
</div>

<div class="px-3 py-2 rounded border-l-4 border-emerald-500 bg-emerald-500/10">
<div class="font-mono text-xs text-emerald-400">Feb 2024</div>
<div class="font-bold">uv</div>
<div class="text-xs opacity-70">a fast pip replacement</div>
</div>

<div class="px-3 py-2 rounded border-l-4 border-emerald-500 bg-emerald-500/10">
<div class="font-mono text-xs text-emerald-400">Aug 2024</div>
<div class="font-bold">uv, project manager</div>
<div class="text-xs opacity-70">projects, lock files, Pythons, tools</div>
</div>

<div class="px-3 py-2 rounded border-l-4 border-emerald-500 bg-emerald-500/10">
<div class="font-mono text-xs text-emerald-400">Mar 2025</div>
<div class="font-bold">PEP 751</div>
<div class="text-xs opacity-70">a standard lock file (pylock.toml)</div>
</div>

</div>

<div class="sources">
Sources: PyPI release histories for <a href="https://pypi.org/project/virtualenv/#history">virtualenv</a>, <a href="https://pypi.org/project/pip/#history">pip</a>, <a href="https://pypi.org/project/pipenv/#history">Pipenv</a>, <a href="https://pypi.org/project/poetry/#history">Poetry</a> ·
<a href="https://www.python.org/downloads/release/python-330/">Python 3.3.0</a> · <a href="https://github.com/conda/conda/blob/main/CHANGELOG.md">conda changelog</a> ·
<a href="https://peps.python.org/pep-0405/">PEP 405</a> · <a href="https://peps.python.org/pep-0518/">PEP 518</a> · <a href="https://discuss.python.org/t/pep-621-round-3/5472/109">PEP 621 acceptance</a> · <a href="https://peps.python.org/pep-0723/">PEP 723</a> · <a href="https://peps.python.org/pep-0751/">PEP 751</a> ·
<a href="https://astral.sh/blog/uv">astral.sh/blog/uv</a> · <a href="https://astral.sh/blog/uv-unified-python-packaging">astral.sh/blog/uv-unified-python-packaging</a>
</div>

<!--
[0:10-0:12] The story, left to right, top to bottom:

- Environments came first (virtualenv, then venv in the standard library).
- pip became the default installer. conda solved non-Python dependencies (C libraries, CUDA) for science.
- pyproject.toml gave projects one config file; Pipenv and Poetry added lock files.
- PEP 621 standardised project metadata, so tools could agree on [project].
- PEP 723 (accepted Jan 2024) standardised single-file scripts that declare their own dependencies.
- uv started as a fast pip replacement (15 Feb 2024; Astral then claimed 8-10x faster than pip without a cache, 80-115x with a warm cache) and became a full project manager (20 Aug 2024).
- PEP 751 (accepted Mar 2025) standardised a lock file format, pylock.toml.
- Exact dates: virtualenv 0.8 on 14 Sep 2007; pip 0.2 on 28 Oct 2008; Python 3.3.0 on 29 Sep 2012; conda 1.0.0 on 6 Sep 2012; PEP 518 created 10 May 2016; Pipenv 0.1.0 on 20 Jan 2017; Poetry 0.1.0 on 28 Feb 2018; PEP 621 accepted 15 Nov 2020.

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
Sources: <a href="https://github.blog/2021-06-29-introducing-github-copilot-ai-pair-programmer/">GitHub blog (Copilot)</a> · <a href="https://openai.com/index/chatgpt/">OpenAI (ChatGPT)</a> · <a href="https://openai.com/index/gpt-4/">OpenAI (GPT-4)</a> · <a href="https://x.com/karpathy/status/1886192184808149383">Karpathy on X</a> (<a href="https://en.wikipedia.org/wiki/Vibe_coding">see also</a>) ·
<a href="https://www.anthropic.com/news/claude-3-7-sonnet">Anthropic (Feb 2025)</a> · <a href="https://www.anthropic.com/news/claude-4">Anthropic (May 2025)</a> · <a href="https://openai.com/index/introducing-o3-and-o4-mini/">OpenAI (Codex CLI)</a>, <a href="https://github.com/openai/codex">github.com/openai/codex</a> · <a href="https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/">Google (Gemini CLI)</a> · <a href="https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation">Linux Foundation (AGENTS.md)</a>
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

<div class="grid grid-cols-2 gap-3 mt-1">

<div class="px-3 py-2 rounded border-l-4 border-gray-400 bg-gray-500/10 text-sm">
<div class="text-xs uppercase tracking-widest opacity-60 mb-1">My course plan, 2023</div>
"...the bulk of the code can be written by GPT-4 or other coding assistants"
</div>

<div class="px-3 py-2 rounded border-l-4 border-pink-500 bg-pink-500/10 text-sm">
<div class="text-xs uppercase tracking-widest text-pink-400 mb-1">2026</div>
Agents write whole features, across many files.
</div>

</div>

<div class="mt-3 font-bold">Typing code is cheap now. The scarce skills are:</div>

<div class="grid grid-cols-3 gap-3 mt-2">

<div class="px-3 py-2 rounded border border-sky-500/30 bg-sky-500/5">
<div class="text-lg font-bold text-sky-400">Specify</div>
<div class="text-sm opacity-70">say exactly what you want</div>
</div>

<div class="px-3 py-2 rounded border border-emerald-500/30 bg-emerald-500/5">
<div class="text-lg font-bold text-emerald-400">Verify</div>
<div class="text-sm opacity-70">check what you got</div>
</div>

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="text-lg font-bold text-orange-400">Explain</div>
<div class="text-sm opacity-70">defend every line</div>
</div>

</div>

<div class="mt-3 text-center">
Type hints and docstrings are how you talk to <b>both</b> the humans and the AI that read your code.
</div>

<div class="grid grid-cols-2 gap-3 mt-3">

<div class="px-3 py-2 rounded border border-gray-500/30 text-sm flex items-center gap-3">
<div class="text-3xl font-bold text-pink-400 shrink-0">84%</div>
<div>of developers use or plan to use AI tools, but more distrust their accuracy (46%) than trust it (33%). <span class="opacity-60">Stack Overflow survey, 2025</span></div>
</div>

<div class="px-3 py-2 rounded border border-gray-500/30 text-sm flex items-center gap-3">
<div class="text-3xl font-bold text-orange-400 shrink-0">19%</div>
<div>slower with AI in an early-2025 trial, while the developers believed AI made them 20% faster. METR now says these results no longer reflect current tools. <span class="opacity-60">METR, 2025-26</span></div>
</div>

</div>

<div class="sources">
Sources: <a href="https://survey.stackoverflow.co/2025/ai">survey.stackoverflow.co/2025/ai</a> · <a href="https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/">METR (July 2025 study)</a> · <a href="https://metr.org/blog/2026-02-24-uplift-update/">METR (Feb 2026 update)</a>
</div>

<!--
[0:13:30-0:15] One slide, one message.

- In 2023 my course plan already said GPT-4 could write the bulk of the code. Three years later, agents write whole features.
- So typing is no longer the bottleneck. Specifying, verifying and explaining are.
- Type hints and docstrings are the cheapest way to specify. They help your teammates, your future self, and the AI.
- Stack Overflow 2025 (about 33,000 answers to each question): 84% use or plan to use AI tools; 46% distrust their accuracy, 33% trust it, 3% highly trust it. Healthy scepticism.
- METR, July 2025: in a randomized trial (16 experienced open-source developers, 246 real issues, mostly Cursor with Claude 3.5/3.7 Sonnet), developers took 19% longer with AI. They had predicted a 24% speedup and afterwards believed they had been 20% faster.
- Be honest about the update: in Feb 2026 METR said those early-2025 results are out of date; its newer late-2025 estimates lean towards small speedups, though METR itself calls them an unreliable signal. The lasting lesson is the perception gap: feeling productive is not the same as being productive, so measure and verify.
-->
