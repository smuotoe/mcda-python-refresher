---
layout: center
class: text-center
title: "Part 2: Code you can read"
---

<div class="absolute inset-0" style="background: radial-gradient(circle at 50% 45%, rgba(249, 115, 22, 0.18), transparent 60%);"></div>

<div class="relative z-10">

<div class="text-sm uppercase tracking-[0.3em] text-orange-400 mb-4">Part 2 · 0:30 - 1:00</div>

<h1 class="!text-6xl font-bold">Code you can read</h1>

<div class="text-xl opacity-80 mt-6">Functions, type hints, docstrings and classes</div>

</div>

<!--
[0:30] Section transition.
-->

---
layout: default
---

# AI writes the code. Why learn to read it?

<div class="grid grid-cols-3 gap-4 mt-6">

<div class="px-4 py-3 rounded border-t-4 border-orange-500 bg-orange-500/10">
<div class="text-xl font-bold text-orange-400">You review it</div>
<div class="text-sm mt-2">AI output is a first draft. Someone has to decide whether it's right before it ships. That's you.</div>
</div>

<div class="px-4 py-3 rounded border-t-4 border-orange-500 bg-orange-500/10">
<div class="text-xl font-bold text-orange-400">You debug it</div>
<div class="text-sm mt-2">When it breaks, the traceback points at a line of code. You need to know what that line does.</div>
</div>

<div class="px-4 py-3 rounded border-t-4 border-orange-500 bg-orange-500/10">
<div class="text-xl font-bold text-orange-400">You own it</div>
<div class="text-sm mt-2">"The AI wrote it" is not an answer in a code review, an exam or an incident report.</div>
</div>

</div>

<div class="mt-10 text-center text-2xl font-bold">
If you can't explain it, you don't own it.
</div>

<div class="mt-3 text-center text-sm opacity-70">
So today is about reading code: fill in a few gaps, then review code an AI wrote.
</div>

<!--
[0:30-0:32] The why for this whole part.

- Agents write most of the code in many teams now. The job shifts from typing code to specifying, reviewing and verifying it.
- You can't review what you can't read. Functions, type hints, docstrings and classes are the building blocks you'll be reading all day.
-->

---
layout: default
---

# Functions: anatomy of a good one

```python
def average(scores: list[float], drop_lowest: bool = False) -> float:
    """Return the mean score, optionally ignoring the lowest one."""
    if not scores:
        raise ValueError("scores must not be empty")
    if drop_lowest and len(scores) > 1:
        scores = sorted(scores)[1:]
    return sum(scores) / len(scores)
```

<div class="grid grid-cols-2 gap-4 mt-3">

<div class="text-sm space-y-1">
<div><span class="text-orange-400 font-bold">Name</span> says what it returns; <span class="text-orange-400 font-bold">type hints</span> say what goes in and out.</div>
<div><span class="text-orange-400 font-bold">Docstring</span>: what it does, in one line or more.</div>
<div><span class="text-orange-400 font-bold">One function, one job.</span> Raise early on bad input.</div>
<div><span class="text-orange-400 font-bold">Return values, don't print them</span>, so other code can use the result.</div>
</div>

<div class="px-3 py-2 rounded border border-red-500/40 bg-red-500/5 text-sm">
<div class="font-bold text-red-400 mb-1">Classic bug: a mutable default</div>

```python
def add_tag(tag: str, tags: list[str] = []):
    tags.append(tag)
    return tags

add_tag("a")  # ['a']
add_tag("b")  # ['a', 'b']  shared list!
```

<div class="text-xs mt-1">The <code>[]</code> is created once, when <code>def</code> runs. Fix: default to <code>None</code> and make a new list inside.</div>
</div>

</div>

<div class="sources">
Sources: <a href="https://docs.python.org/3/library/typing.html">docs.python.org/3/library/typing</a> · <a href="https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects">Python FAQ: why are default values shared between objects?</a>
</div>

<!--
[0:32-0:35] Walk through the function top to bottom.

- Name + type hints are the contract: someone (or an AI) can call it correctly without reading the body.
- Guard clause: raise immediately on bad input instead of nesting the happy path in if/else.
- `scores = sorted(scores)[1:]` builds a new list; we never modify the caller's list.
- Mutable default: ask the room what the second call returns before pointing at the comment. You'll hunt for this exact bug in Exercise 2.
- Modern hint syntax if asked: `list[str]`, `dict[str, int]`, `str | None`.
-->

---
layout: default
---

# Demo: type hints and docstrings in VS Code

<div class="grid grid-cols-5 gap-4 mt-1">

<div class="col-span-3">

<div class="text-sm font-bold text-red-400 mb-1">Before: the editor knows nothing</div>

```python
def average(scores, drop_lowest=False):
```

<div class="text-sm font-bold text-emerald-400 mt-2 mb-1">After: the editor knows everything</div>

```python
def average(
    scores: list[float], drop_lowest: bool = False
) -> float:
    """Return the mean score, optionally ignoring the lowest.

    Args:
        scores: The scores to average. Must not be empty.
        drop_lowest: If True, ignore the lowest score.

    Returns:
        The mean of the scores that count.
    """
```

</div>

<div class="col-span-2 space-y-2 text-sm">

<div class="px-3 py-2 rounded border-l-4 border-orange-500 bg-orange-500/10"><b>Hover</b> over <code>average</code>: the signature and docstring appear, nicely formatted.</div>

<div class="px-3 py-2 rounded border-l-4 border-orange-500 bg-orange-500/10"><b>Autocomplete:</b> type <code>result.</code> and VS Code lists what a <code>float</code> can do.</div>

<div class="px-3 py-2 rounded border-l-4 border-orange-500 bg-orange-500/10"><b>Red squiggles:</b> <code>average("90")</code> is flagged before you run anything.</div>

<div class="px-3 py-2 rounded border-l-4 border-orange-500 bg-orange-500/10"><b>Google style:</b> a summary line, then <b>Args</b>, <b>Returns</b>, <b>Raises</b>.</div>

<div class="px-3 py-2 rounded border-l-4 border-sky-500 bg-sky-500/10">Agents read the same hints and docstrings, and write them for you if you ask. You still need to read them.</div>

</div>

</div>

<div class="sources">
Sources: <a href="https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings">Google Python Style Guide 3.8</a> · <a href="https://code.visualstudio.com/docs/python/editing">VS Code: Python editing</a>
</div>

<!--
[0:35-0:40] Live in VS Code with demos/type_hints.py. Students can follow along.

1. Hover over `average`: almost no information; the parameter types are unknown.
2. On the `result = average(...)` line, type `result.` underneath: no useful suggestions, because the editor can't tell what `average` returns.
3. Add the type hints from the slide. Hover again: now it shows `(scores: list[float], drop_lowest: bool = False) -> float`. `result.` now lists float methods (is_integer, hex, ...).
4. Add the docstring. Hover again: the docstring renders under the signature, Args and all.
5. Type `average("90")` on a new line: red squiggle. Hover the squiggle to read the error. Delete the line.
6. Optional: `help(average)` in a Python REPL (`uv run python`) prints the same docstring.

Why the squiggle appears: pyproject.toml sets `[tool.pyright] typeCheckingMode = "basic"`, which VS Code's Python extension (Pylance) reads. Without it, Pylance's default mode doesn't report type mismatches.

The honest framing: few people hand-write full docstrings any more; agents write them. But hints and docstrings are how you, your editor and your agent understand code you didn't write. In Part 3 we make the agent write them every time.
-->

---
layout: default
---

# Classes: data plus behaviour

<div class="grid grid-cols-5 gap-4 mt-1">

<div class="col-span-2 text-sm space-y-3">

<div><b class="text-orange-400">Use a class</b> when data and the operations on it belong together. Otherwise, plain functions.</div>

<div><b class="text-orange-400"><code>@dataclass</code></b> writes <code>__init__</code>, <code>__repr__</code> and <code>__eq__</code> from the fields you list.</div>

<div><b class="text-orange-400"><code>field(default_factory=list)</code></b>: a new list for every instance. The dataclass version of the mutable-default fix.</div>

<div><b class="text-orange-400"><code>@property</code></b>: a computed value that reads like an attribute and never goes stale.</div>

</div>

<div class="col-span-3">

```python
from dataclasses import dataclass, field


@dataclass
class Playlist:
    name: str
    songs: list[str] = field(default_factory=list)

    def add(self, song: str) -> None:
        self.songs.append(song)

    @property
    def size(self) -> int:
        return len(self.songs)


focus = Playlist("Focus")
focus.add("Clair de Lune")
print(focus)       # Playlist(name='Focus', songs=['Clair de Lune'])
print(focus.size)  # 1
```

<div class="text-xs opacity-60 mt-1">Docstrings left out to fit the slide.</div>

</div>

</div>

<div class="sources">
Sources: <a href="https://docs.python.org/3/library/dataclasses.html">docs.python.org/3/library/dataclasses</a>
</div>

<!--
[0:40-0:44] Classes in four minutes.

- Rule of thumb: if you keep passing the same data into a group of functions, that's a class.
- @dataclass: you list the fields, Python writes the boring methods. `print(focus)` shows the free __repr__.
- `songs: list[str] = []` would be the mutable-default bug again; dataclasses actually refuse it with a ValueError. `field(default_factory=list)` calls list() for each new Playlist.
- @property: `focus.size` (no parentheses) is computed every time, so it can't go stale.
- Exercise 1 uses all three: a dataclass, a method and a property.
-->

---
layout: default
---

# Exercise 1: fill in the gradebook (7 min)

<div class="text-sm opacity-70 -mt-3 mb-3">File: <code>exercises/gradebook.py</code> · read each docstring, then write the body</div>

<div class="grid grid-cols-3 gap-3">

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400 font-mono text-sm">letter_grade(average)</div>
<ul class="text-sm mt-2">
<li>90+ is A, 80+ B, 70+ C, 60+ D</li>
<li>anything lower is F</li>
</ul>
<div class="font-mono text-xs opacity-80 mt-2">letter_grade(59.5) -> "F"</div>
</div>

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400 font-mono text-sm">Student.add_score(score)</div>
<ul class="text-sm mt-2">
<li>append to <code>self.scores</code></li>
<li><code>ValueError</code> if the score is outside 0-100</li>
</ul>
</div>

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400 font-mono text-sm">Student.average</div>
<ul class="text-sm mt-2">
<li>a property</li>
<li>the mean of the scores</li>
<li><code>0.0</code> if there are none</li>
</ul>
</div>

</div>

<div class="mt-4 px-4 py-2 rounded bg-gray-500/10 flex items-center gap-4">
<div class="text-sm font-bold">Check:</div>
<div class="font-mono text-sm">uv run exercises/gradebook.py</div>
<div class="text-sm opacity-70">and compare with the <code># expected:</code> comments</div>
</div>

<div class="mt-3 text-sm opacity-70 text-center">A <code>NotImplementedError: TODO</code> on the first run is expected: that's your first task.</div>

<!--
[0:44-0:51] Exercise 1. Walk around.

- letter_grade: an if/elif chain is fine. Neater: `for cutoff, letter in ((90, "A"), (80, "B"), (70, "C"), (60, "D")): if average >= cutoff: return letter`, then `return "F"`.
- add_score: validate first (`if not 0 <= score <= 100: raise ValueError(...)`), then `self.scores.append(score)`.
- average: `if not self.scores: return 0.0`, then `sum(self.scores) / len(self.scores)`. No parentheses when calling it: `ada.average`.
- The `grace.scores` line prints [] thanks to default_factory: each student gets their own list.
- Expected for Ada after 90, 85, 100: 91.66666666666667 A.
-->

---
layout: default
---

# Exercise 2: review the AI's code (8 min)

<div class="text-sm opacity-70 -mt-3 mb-3">File: <code>exercises/review.py</code></div>

<div class="grid grid-cols-5 gap-4">

<div class="col-span-3 space-y-2">

<div class="px-3 py-2 rounded border-l-4 border-orange-500 bg-orange-500/10">
<b>An AI agent wrote this file.</b> It runs without crashing, the type hints and docstrings look great, and it has <b>three bugs</b>.
</div>

<div class="px-3 py-2 rounded border-l-4 border-sky-500 bg-sky-500/10 text-sm">
<b>1.</b> Run it and compare with the <code># expected:</code> comments.<br/>
<b>2.</b> For each wrong line of output, find the line of code responsible.<br/>
<b>3.</b> Fix it, rerun, repeat.
</div>

<div class="px-3 py-2 rounded bg-gray-500/10 text-sm">
<b>Hint:</b> your editor already flags one of the bugs. The other two you have to read for.
</div>

</div>

<div class="col-span-2">

<div class="font-mono text-sm mb-1">uv run exercises/review.py</div>

```text
['90', '85', '100']
90
['Ada']
['Great work']
['Great work', 'See me after class']
```

<div class="text-xs opacity-70 mt-1">What you'll see. Every line here is wrong.</div>

</div>

</div>

<!--
[0:51-1:00] Exercise 2, then a 1-minute debrief.

Important: keep YOUR copy of review.py unfixed. The Part 3 demo runs the tools on it.

The bugs:
1. parse_scores returns `part.strip()`, which is a string, not a float. Fix: `float(part)`. The editor flags this one (the return type doesn't match `list[float]`). It's also why best_score prints 90: `max` on strings compares them alphabetically, and "9" sorts after "1".
2. top_students returns `ranked[: n - 1]`: off by one, so asking for 2 students returns 1. Fix: `ranked[:n]`.
3. add_comment has a mutable default (`comments: list[str] = []`), so the second call still contains "Great work". Fix: `comments: list[str] | None = None` and build a new list.

Debrief question: the docstrings were perfect and the type hints were right. Did that make the code correct? (No. It made it easier to see where the code disagreed with its own description.)
-->
