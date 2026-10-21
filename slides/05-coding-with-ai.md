---
layout: center
class: text-center
---

<div class="absolute inset-0" style="background: radial-gradient(circle at 50% 45%, rgba(236, 72, 153, 0.18), transparent 60%);"></div>

<div class="relative z-10">

<div class="text-sm uppercase tracking-[0.3em] text-pink-400 mb-4">Part 5 · 1:15 - 1:27</div>

<h1 class="!text-6xl font-bold">Specify, Generate, Verify, Explain</h1>

<div class="text-xl opacity-80 mt-6">Coding with AI without losing ownership of your code</div>

</div>

<!--
[1:15] Section transition. Everything so far (type hints, docstrings, small functions) pays off here.
-->

---
layout: default
---

# The loop

<div class="grid grid-cols-4 gap-3 mt-6">

<div class="px-3 py-3 rounded border-t-4 border-sky-500 bg-sky-500/10">
<div class="text-xs font-mono opacity-60">1</div>
<div class="text-xl font-bold text-sky-400">Specify</div>
<div class="text-sm mt-2">Signature, type hints and a docstring that say exactly what you want.</div>
</div>

<div class="px-3 py-3 rounded border-t-4 border-purple-500 bg-purple-500/10">
<div class="text-xs font-mono opacity-60">2</div>
<div class="text-xl font-bold text-purple-400">Generate</div>
<div class="text-sm mt-2">Any AI tool: chat, Copilot, Claude Code, Codex, Gemini CLI.</div>
</div>

<div class="px-3 py-3 rounded border-t-4 border-emerald-500 bg-emerald-500/10">
<div class="text-xs font-mono opacity-60">3</div>
<div class="text-xl font-bold text-emerald-400">Verify</div>
<div class="text-sm mt-2">Run it, compare with the expected output, and read the code.</div>
</div>

<div class="px-3 py-3 rounded border-t-4 border-orange-500 bg-orange-500/10">
<div class="text-xs font-mono opacity-60">4</div>
<div class="text-xl font-bold text-orange-400">Explain</div>
<div class="text-sm mt-2">You can defend every line to a colleague.</div>
</div>

</div>

<div class="mt-8 text-center text-2xl font-bold">
If you can't explain it, you don't own it.
</div>

<div class="mt-3 text-center text-sm opacity-70">
Not happy at step 3 or 4? Go back to step 1: the spec was ambiguous.
</div>

<!--
[1:15-1:17] The habit I want you to leave with.

- Specify: the same things we just practised. A docstring is a prompt that also documents your code.
- Generate: the tool doesn't matter much. Use what you have.
- Verify: run it against known inputs and outputs, and actually read it.
- Explain: in my course, "the AI wrote it" is not an answer. If you can't explain a line, you don't own it yet.
-->

---
layout: default
---

# Exercise 4: spec first (7 min)

<div class="text-sm opacity-70 -mt-3 mb-2">File: <code>exercises/spec_first.py</code> · <code>parse_duration(text: str) -> int</code> returns minutes</div>

<div class="grid grid-cols-5 gap-4">

<div class="col-span-3 space-y-2">

<div class="px-3 py-2 rounded border-l-4 border-purple-500 bg-purple-500/10 text-sm">
<b>Step 1: vague prompt.</b> Ask any AI: <i>"Write a Python function that parses durations like 1h30m."</i> Paste its answer over the stub, run the file, and compare.
</div>

<div class="px-3 py-2 rounded border-l-4 border-sky-500 bg-sky-500/10 text-sm">
<b>Step 2: full spec.</b> Give the AI the whole docstring from the file (the rules). Paste, rerun, compare again.
</div>

<div class="px-3 py-2 rounded border-l-4 border-orange-500 bg-orange-500/10 text-sm">
<b>Step 3: explain</b> every line to your neighbour.
</div>

<div class="px-3 py-2 rounded bg-gray-500/10 text-sm">
<b>Lesson:</b> wherever your spec is ambiguous, the AI guesses.
</div>

</div>

<div class="col-span-2">

<div class="font-mono text-sm mb-1">uv run exercises/spec_first.py</div>

```text
  '1h30m' -> 90
     '2h' -> 120
    '45m' -> 45
 '1H 30m' -> 90
  '1h90m' -> ValueError
   '1.5h' -> ValueError
  '30m1h' -> ValueError
       '' -> ValueError
```

<div class="text-xs opacity-70 mt-1">Expected output. Vague prompts usually get some of the last four wrong.</div>

</div>

</div>

<!--
[1:17-1:24] Exercise 4.

- Step 1 usually "works" for 1h30m, 2h and 45m, then accepts 1h90m (150), 1.5h, or 30m1h, or crashes on the empty string with the wrong error.
- Step 2: the docstring's rules (order, whole numbers, minutes below 60 with hours, case-insensitive, spaces) remove the guesswork. Most tools then produce a version that matches.
- Ask a pair to read their final version aloud and explain the regex or the parsing logic.
- No AI access? Pair with a neighbour, or write it yourself from the docstring: that's the same skill.
-->

---
layout: default
---

# Guardrails

<div class="grid grid-cols-2 gap-4 mt-1">

<div class="px-3 py-2 rounded border border-pink-500/30 bg-pink-500/5">
<div class="font-bold text-pink-400 mb-1">AGENTS.md: rules your agent reads</div>
<div class="text-xs opacity-70 mb-1">A plain Markdown file in the repo root that coding agents read before they work. From ours:</div>

```markdown
- Use uv: `uv add <package>` to add dependencies
  and `uv run <file>` to run code. Never call pip directly.
- Don't add a dependency without asking, and check
  that it exists on PyPI first.
```

</div>

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400 mb-1">Check that a package exists before <code>uv add</code></div>
<div class="text-sm">AIs invent package names. Attackers register those names with malware ("slopsquatting").</div>
<div class="text-xs mt-1 opacity-80">A study of 16 code LLMs and 576,000 code samples found hallucinated packages in at least 5.2% (commercial) and 21.7% (open-source) of cases: 205,474 unique fake names.</div>
<div class="font-mono text-xs mt-2">uv run demos/pypi_check.py some-package</div>
</div>

<div class="px-3 py-2 rounded border border-emerald-500/30 bg-emerald-500/5">
<div class="font-bold text-emerald-400 mb-1">Secrets stay out of git</div>
<div class="text-sm">API keys go in <code>.env</code>, and <code>.env</code> goes in <code>.gitignore</code>. Read them from environment variables.</div>
</div>

<div class="px-3 py-2 rounded border border-sky-500/30 bg-sky-500/5">
<div class="font-bold text-sky-400 mb-1">Mind what you paste</div>
<div class="text-sm">Don't paste private data, client code or credentials into public chat tools.</div>
</div>

</div>

<div class="sources">
Sources: <a href="https://agents.md/">agents.md</a> · Spracklen et al., <a href="https://arxiv.org/abs/2406.10279">"We Have a Package for You!", USENIX Security 2025 (arXiv 2406.10279)</a>
</div>

<!--
[1:24-1:27] Four habits that keep AI-assisted work safe.

- AGENTS.md: open the repo's file. Agents such as Codex, Cursor and Gemini CLI read it automatically; others can be pointed at it. It's where "use uv, never pip" lives.
- Package hallucination: the paper tested 16 models on 576,000 generated samples. Attackers watch for commonly hallucinated names and publish malware under them. Run the PyPI checker, or at least look at the PyPI page (age, downloads, repo link) before `uv add`.
- Secrets: .env plus .gitignore (our repo's .gitignore already lists .env). Never hard-code keys.
- Public chat tools may keep or train on what you paste. Use the tools your employer or school approves for private code.
-->
