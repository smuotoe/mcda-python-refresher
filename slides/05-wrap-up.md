---
layout: default
---

# Checklist for every project

<div class="mt-6 space-y-4 text-lg">

<div class="flex items-start gap-4">
<span class="inline-block w-5 h-5 mt-1 shrink-0 rounded-sm border-2 border-teal-400"></span>
<div>A <b>uv project</b>: <code>pyproject.toml</code> and <code>uv.lock</code>, and no more "which pip?"</div>
</div>

<div class="flex items-start gap-4">
<span class="inline-block w-5 h-5 mt-1 shrink-0 rounded-sm border-2 border-teal-400"></span>
<div>An <b>AGENTS.md</b> with your rules, so every agent works your way</div>
</div>

<div class="flex items-start gap-4">
<span class="inline-block w-5 h-5 mt-1 shrink-0 rounded-sm border-2 border-teal-400"></span>
<div><b>Ruff and a type checker</b> clean before you call it done</div>
</div>

<div class="flex items-start gap-4">
<span class="inline-block w-5 h-5 mt-1 shrink-0 rounded-sm border-2 border-teal-400"></span>
<div><b>Small functions</b> with type hints and docstrings, and you can explain every line</div>
</div>

<div class="flex items-start gap-4">
<span class="inline-block w-5 h-5 mt-1 shrink-0 rounded-sm border-2 border-teal-400"></span>
<div><b>No secrets in code</b>: <code>.env</code> for keys, read from environment variables</div>
</div>

</div>

<!--
[1:25-1:27] If you remember one slide, make it this one.

- Every item is something we did today. Copy starter/AGENTS.md into your next project and make it yours.
-->

---
layout: default
---

# Resources

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<div class="font-bold text-emerald-400 mb-2">uv and Ruff</div>

<div class="text-sm space-y-2">
<div><a href="https://docs.astral.sh/uv/" class="inline-block">docs.astral.sh/uv</a><br/><span class="opacity-70">guides for projects, scripts, tools and Python versions</span></div>
<div><a href="https://docs.astral.sh/ruff/" class="inline-block">docs.astral.sh/ruff</a><br/><span class="opacity-70">every lint rule, with examples of the fix</span></div>
</div>

</div>

<div>

<div class="font-bold text-orange-400 mb-2">Readable Python and agents</div>

<div class="text-sm space-y-2">
<div><a href="https://docs.python.org/3/library/typing.html" class="inline-block">Python typing documentation</a><br/><span class="opacity-70">every type hint, with examples</span></div>
<div><a href="https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings" class="inline-block">Google Python Style Guide: docstrings</a><br/><span class="opacity-70">Args, Returns, Raises, with examples</span></div>
<div><a href="https://agents.md/" class="inline-block">agents.md</a><br/><span class="opacity-70">the AGENTS.md format, and which agents read it</span></div>
</div>

</div>

</div>

<div class="mt-8 px-4 py-3 rounded border-l-4 border-teal-500 bg-teal-500/10">
<div class="font-bold">Today's exercises and slides</div>
<a href="https://github.com/smuotoe/mcda-python-refresher" class="inline-block font-mono text-sm">github.com/smuotoe/mcda-python-refresher</a>
</div>

<!--
[1:27-1:28] Everything is linked from the repo README too.

- Finish any exercises you didn't get to; each file prints its expected output.
-->

---
layout: center
class: text-center
title: Thank you
---

<div class="absolute inset-0" style="background: radial-gradient(circle at 18% 22%, rgba(16, 185, 129, 0.18), transparent 45%), radial-gradient(circle at 82% 78%, rgba(139, 92, 246, 0.18), transparent 45%);"></div>

<div class="relative z-10">

<h1 class="!text-6xl font-bold">Thank you</h1>

<div class="text-2xl opacity-80 mt-6">Questions?</div>

<div class="mt-8 text-sm opacity-70 font-mono">github.com/smuotoe/mcda-python-refresher</div>

</div>

<!--
[1:28-1:30] Thank them. Take questions.

- Remind them: finish the exercises and keep uv installed.
-->
