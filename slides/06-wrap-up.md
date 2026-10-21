---
layout: default
---

# Checklist for every project

<div class="mt-6 space-y-4 text-lg">

<div class="flex items-start gap-4">
<span class="inline-block w-5 h-5 mt-1 shrink-0 rounded-sm border-2 border-teal-400"></span>
<div>A <b>uv project</b>, with <code>pyproject.toml</code> and <code>uv.lock</code> committed</div>
</div>

<div class="flex items-start gap-4">
<span class="inline-block w-5 h-5 mt-1 shrink-0 rounded-sm border-2 border-teal-400"></span>
<div>A <b>README</b> with setup and run steps <span class="text-base opacity-70">(<code>uv sync</code>, <code>uv run ...</code>)</span></div>
</div>

<div class="flex items-start gap-4">
<span class="inline-block w-5 h-5 mt-1 shrink-0 rounded-sm border-2 border-teal-400"></span>
<div><b>Small functions</b> with type hints and Google-style docstrings</div>
</div>

<div class="flex items-start gap-4">
<span class="inline-block w-5 h-5 mt-1 shrink-0 rounded-sm border-2 border-teal-400"></span>
<div><b>No secrets in code</b>: <code>.env</code> for keys, and <code>.env</code> in <code>.gitignore</code></div>
</div>

</div>

<div class="mt-10 text-center text-sm opacity-70">
This is what I'll look for in January.
</div>

<!--
[1:27-1:28] If you remember one slide, make it this one.

- Every item is something we did today.
- A teammate should be able to clone, `uv sync`, and run your project from the README alone.
-->

---
layout: default
---

# Resources

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<div class="font-bold text-emerald-400 mb-2">uv</div>

<div class="text-sm space-y-2">
<div><a href="https://docs.astral.sh/uv/" class="inline-block">docs.astral.sh/uv</a><br/><span class="opacity-70">guides for projects, scripts, tools and Python versions</span></div>
<div><a href="https://peps.python.org/pep-0723/" class="inline-block">PEP 723: inline script metadata</a><br/><span class="opacity-70">the <code># /// script</code> block</span></div>
</div>

</div>

<div>

<div class="font-bold text-orange-400 mb-2">Writing clear Python</div>

<div class="text-sm space-y-2">
<div><a href="https://docs.python.org/3/library/typing.html" class="inline-block">Python typing documentation</a><br/><span class="opacity-70">every type hint, with examples</span></div>
<div><a href="https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings" class="inline-block">Google Python Style Guide: docstrings</a><br/><span class="opacity-70">Args, Returns, Raises, with examples</span></div>
</div>

</div>

</div>

<div class="mt-8 px-4 py-3 rounded border-l-4 border-teal-500 bg-teal-500/10">
<div class="font-bold">Today's exercises and slides</div>
<a href="https://github.com/smuotoe/mcda-python-refresher" class="inline-block font-mono text-sm">github.com/smuotoe/mcda-python-refresher</a>
</div>

<!--
[1:28-1:29] Everything is linked from the repo README too.

- Finish any exercises you didn't get to; each file prints its expected output.
-->

---
layout: center
class: text-center
---

<div class="absolute inset-0" style="background: radial-gradient(circle at 18% 22%, rgba(16, 185, 129, 0.18), transparent 45%), radial-gradient(circle at 82% 78%, rgba(139, 92, 246, 0.18), transparent 45%);"></div>

<div class="relative z-10">

<h1 class="!text-6xl font-bold">Thank you</h1>

<div class="text-2xl opacity-80 mt-6">Questions?</div>

<div class="text-xl mt-10 text-teal-400">See you in January.</div>

<div class="mt-8 text-sm opacity-70 font-mono">github.com/smuotoe/mcda-python-refresher</div>

</div>

<!--
[1:29-1:30] Thank them. Take questions.

- Remind them: finish the exercises and keep uv installed. See you in January.
-->
