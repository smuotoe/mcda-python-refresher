---
layout: default
---

# Get the exercises

<div class="grid grid-cols-5 gap-5 mt-2">

<div class="col-span-3">

```bash
git clone https://github.com/smuotoe/modern-python-refresher
cd modern-python-refresher
uv sync
uv run exercises/functions.py
```

<div class="mt-3 px-3 py-2 rounded border-l-4 border-emerald-500 bg-emerald-500/10">
<b>One command, my exact environment.</b> <code>uv sync</code> reads <code>uv.lock</code> and <code>.python-version</code>, and downloads Python 3.13 if you don't have it.
</div>

<div class="mt-3 text-sm opacity-80">
A <code>NotImplementedError: TODO</code> on the first run is expected: that's your first task.
</div>

<div class="mt-2 text-xs opacity-70">No git? On the GitHub page: <b>Code &gt; Download ZIP</b>, unzip, and <code>cd</code> into the folder.</div>

</div>

<div class="col-span-2">

```text
exercises/
  functions.py     Exercise 1
  docstrings.py    Exercise 2
  classes.py       Exercise 3
  spec_first.py    Exercise 4 (with AI)
demos/
  pypi_check.py
AGENTS.md
pyproject.toml
uv.lock
```

<div class="text-sm opacity-80 mt-2">Each exercise: fill in the TODOs, run the file, compare with the <code># expected:</code> comments.</div>

</div>

</div>

<!--
[0:40-0:43] Everyone clones and syncs.

- This is the payoff of the uv section: one `uv sync` and everyone has the same Python and packages.
- If git isn't installed: Download ZIP works.
- Running functions.py now prints two add_tag results and then stops at slugify's NotImplementedError. That's expected.
- No test framework today: every exercise prints its results, and the expected values are written in comments next to each print.
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
<div><span class="text-orange-400 font-bold">Name</span> says what it returns; <span class="text-orange-400 font-bold">typed parameters</span> and a <span class="text-orange-400 font-bold">return type</span> say what goes in and out.</div>
<div><span class="text-orange-400 font-bold">Docstring</span>: one line on what it does.</div>
<div><span class="text-orange-400 font-bold">One function, one job.</span> Raise early on bad input.</div>
<div><span class="text-orange-400 font-bold">Return values, don't print them</span>, so other code can use the result.</div>
</div>

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5 text-sm">
<div class="font-bold text-orange-400 mb-1">Modern type hints</div>
<div class="font-mono text-xs space-y-1">
<div>names: list[str]</div>
<div>counts: dict[str, int]</div>
<div>nickname: str | None = None</div>
<div>def first[T](items: list[T]) -> T: ...  <span class="opacity-60"># Python 3.12+</span></div>
</div>
</div>

</div>

<div class="sources">
Sources: <a href="https://docs.python.org/3/library/typing.html">docs.python.org/3/library/typing</a> · <a href="https://peps.python.org/pep-0695/">PEP 695 (type parameter syntax, Python 3.12)</a>
</div>

<!--
[0:43-0:46] Walk through the function top to bottom.

- Name + type hints are the contract. Someone (or an AI) can call it correctly without reading the body.
- Guard clause: raise immediately on bad input instead of nesting the happy path in if/else.
- `scores = sorted(scores)[1:]` builds a new list; we never modify the caller's list.
- Return, don't print: printing makes the result useless to the code that called you.
- Type hints: built-in generics (`list[str]`), `X | None` for "might be missing", and the 3.12 generic syntax `def first[T](...)`, which you'll use in Exercise 1.
-->

---
layout: default
---

# Pitfall: mutable default arguments

<div class="grid grid-cols-2 gap-5 mt-2">

<div>

```python
def add_tag(tag: str, tags: list[str] = []) -> list[str]:
    tags.append(tag)
    return tags

add_tag("a")  # ['a']
add_tag("b")  # ['a', 'b']  the default list is shared!
```

</div>

<div class="space-y-3">

<div class="px-3 py-2 rounded border-l-4 border-red-500 bg-red-500/10 text-sm">
<b>Why:</b> the default <code>[]</code> is created once, when <code>def</code> runs. Every call that uses the default gets the <i>same</i> list.
</div>

<div class="px-3 py-2 rounded border-l-4 border-emerald-500 bg-emerald-500/10 text-sm">
<b>Fix:</b> default to <code>None</code>, and create a new list inside the function.
</div>

<div class="text-sm opacity-70">Linters catch this: Ruff reports it as rule <code>B006</code>.</div>

</div>

</div>

<div class="sources">
Sources: <a href="https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects">Python FAQ: why are default values shared between objects?</a> · <a href="https://docs.astral.sh/ruff/rules/mutable-argument-default/">Ruff rule B006</a>
</div>

<!--
[0:46-0:48] The classic Python bug.

- Ask the room what the second call returns before revealing the comment.
- Default values are evaluated once, at function definition time. Lists and dicts are mutable, so state leaks between calls.
- The fix is the pattern you'll write in Exercise 1. Bonus point: don't modify the caller's list either; return a new one.
-->

---
layout: default
---

# Exercise 1: functions (8 min)

<div class="text-sm opacity-70 -mt-3 mb-3">File: <code>exercises/functions.py</code></div>

<div class="grid grid-cols-3 gap-3">

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400 font-mono text-sm">slugify(title: str) -> str</div>
<ul class="text-sm mt-2">
<li>lowercase</li>
<li>every run of characters that aren't letters or digits becomes one <code>-</code></li>
<li>strip <code>-</code> from both ends</li>
<li>no accent handling</li>
</ul>
<div class="font-mono text-xs opacity-80 mt-2">"Hello, World!" -> hello-world</div>
</div>

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400 font-mono text-sm">add_tag(tag, tags=[])</div>
<ul class="text-sm mt-2">
<li>run the file first</li>
<li>the second call returns <code>['python', 'uv']</code> instead of <code>['uv']</code></li>
<li>fix the mutable default</li>
</ul>
</div>

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400 font-mono text-sm">chunk[T](items, size)</div>
<ul class="text-sm mt-2">
<li>split into lists of length <code>size</code></li>
<li>the last chunk may be shorter</li>
<li><code>ValueError</code> if <code>size</code> &lt; 1</li>
</ul>
<div class="font-mono text-xs opacity-80 mt-2">[1, 2, 3, 4, 5], 2 -> [[1, 2], [3, 4], [5]]</div>
</div>

</div>

<div class="mt-4 px-4 py-2 rounded bg-gray-500/10 flex items-center gap-4">
<div class="text-sm font-bold">Check:</div>
<div class="font-mono text-sm">uv run exercises/functions.py</div>
<div class="text-sm opacity-70">and compare with the <code># expected:</code> comments</div>
</div>

<!--
[0:48-0:56] Exercise 1.

- slugify hint: the `re` module, `re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")`. Let them find it; give the hint after 3 minutes.
- add_tag: the expected output is ['python'] then ['uv']. Fix with `tags: list[str] | None = None` and build a new list.
- chunk: `[items[i:i + size] for i in range(0, len(items), size)]`, after the size check.
- The `[T]` after `chunk` is the Python 3.12 generic syntax: the output list holds the same type as the input.
-->

---
layout: default
---

# Docstrings: written for humans and for AI

<div class="grid grid-cols-5 gap-4 mt-1">

<div class="col-span-2 text-sm space-y-2">

<div class="font-bold text-orange-400">Why they matter more now</div>

<div>Shown by <code>help()</code> and by IDE hovers</div>
<div>Turned into documentation by doc generators</div>
<div>Read by AI assistants as the spec for your code</div>
<div>Frameworks such as LangChain and MCP build an LLM's tool descriptions straight from your <b>type hints and docstrings</b></div>

<div class="pt-2 font-bold text-orange-400">Google style</div>
<div><b>Summary line</b>, then <b>Args</b>, <b>Returns</b>, <b>Raises</b></div>

</div>

<div class="col-span-3">

```python
def apply_discount(price: float, percent: float) -> float:
    """Apply a percentage discount to a price.

    Args:
        price: Original price.
        percent: Discount percentage between 0 and 100.

    Returns:
        The discounted price, rounded to 2 decimal places.

    Raises:
        ValueError: If percent is outside 0-100.
    """
```

</div>

</div>

<div class="sources">
Sources: <a href="https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings">Google Python Style Guide 3.8</a> · <a href="https://python.langchain.com/docs/how_to/custom_tools/">LangChain: custom tools</a> · <a href="https://github.com/modelcontextprotocol/python-sdk">MCP Python SDK</a>
</div>

<!--
[0:56-0:59] Docstrings used to be "nice to have". Now more readers depend on them.

- `help(apply_discount)` in a REPL, or hover in VS Code: that's the docstring.
- AI assistants read docstrings and type hints to understand what your code should do.
- LangChain's @tool and MCP's FastMCP turn a Python function into a tool an LLM can call: the name, the docstring (description) and the type hints (input schema) are all the model sees.
- Google style: one-line summary, blank line, then Args / Returns / Raises sections. Describe meaning and constraints, not the types (the hints already say that).
-->

---
layout: default
---

# Exercise 2: docstrings (5 min)

<div class="text-sm opacity-70 -mt-3 mb-3">File: <code>exercises/docstrings.py</code></div>

<div class="grid grid-cols-2 gap-4">

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400 mb-1">The task</div>
<div class="text-sm">Both functions work, but have no docstrings. Add a Google-style docstring to each:</div>
<ul class="text-sm mt-1">
<li><code>apply_discount(price, percent)</code></li>
<li><code>split_full_name(full_name)</code></li>
</ul>
<div class="text-sm mt-1">Summary line, then Args, Returns and Raises. Read the code to find what each one raises.</div>
</div>

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400 mb-1">Check</div>

<div class="font-mono text-sm">uv run exercises/docstrings.py</div>

<div class="text-sm mt-1">It prints each docstring. <code>None</code> means you're not done yet.</div>

<div class="text-sm mt-3 opacity-80"><b>Tip:</b> hover over the function name in VS Code to see your docstring as others will.</div>
</div>

</div>

<!--
[0:59-1:04] Exercise 2.

- apply_discount raises ValueError if percent is outside 0-100.
- split_full_name returns a (first names, last name) tuple and raises ValueError if there are fewer than two names. "Mary Ann Smith" -> ("Mary Ann", "Smith").
- Good docstrings describe behaviour and edge cases, not the implementation.
-->

---
layout: default
---

# Classes: state plus behaviour

<div class="grid grid-cols-5 gap-4 mt-1">

<div class="col-span-2 text-sm space-y-2">

<div><b class="text-orange-400">Use a class</b> when data and the operations on it belong together. Otherwise, plain functions.</div>

<div><b class="text-orange-400">Anatomy:</b> a simple <code>__init__</code>, methods, <code>@property</code> for computed values, dunder methods such as <code>__len__</code> and <code>__repr__</code>.</div>

<div><b class="text-orange-400"><code>@dataclass</code></b> for data containers:</div>

```python
@dataclass(frozen=True)
class Song:
    title: str
    seconds: int
```

<div><code>frozen=True</code>: immutable and hashable.</div>

<div><b class="text-orange-400">Composition over inheritance:</b> a Playlist <i>has</i> Songs; it doesn't extend <code>list</code>.</div>

</div>

<div class="col-span-3">

```python
class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self._songs: list[Song] = []

    def add(self, song: Song) -> None:
        self._songs.append(song)

    @property
    def total_seconds(self) -> int:
        return sum(song.seconds for song in self._songs)

    def __len__(self) -> int:
        return len(self._songs)

    def __repr__(self) -> str:
        return f"Playlist({self.name!r}, {len(self)} songs)"
```

<div class="text-xs opacity-60 mt-1">Docstrings omitted to fit the slide.</div>

</div>

</div>

<div class="sources">
Sources: <a href="https://docs.python.org/3/library/dataclasses.html">docs.python.org/3/library/dataclasses</a>
</div>

<!--
[1:04-1:07] Classes in five minutes.

- Rule of thumb: if you keep passing the same data into a group of functions, that's a class.
- Keep __init__ boring: store arguments, set up empty state. No network calls, no heavy work.
- @property: `playlist.total_seconds` reads like an attribute but is computed, so it can never go stale.
- __len__ makes `len(playlist)` work; __repr__ makes debugging output readable.
- @dataclass writes __init__, __repr__ and __eq__ for you. frozen=True makes instances immutable and hashable, so they can be dict keys (you'll need that in Exercise 3).
- Composition: Playlist holds a list of Songs and exposes only what it needs.
-->

---
layout: default
---

# Exercise 3: classes (8 min)

<div class="text-sm opacity-70 -mt-3 mb-3">File: <code>exercises/classes.py</code></div>

<div class="grid grid-cols-2 gap-4">

<div class="px-3 py-2 rounded border border-gray-500/30 bg-gray-500/5">
<div class="font-bold mb-1">Given: <code>Product</code></div>

```python
@dataclass(frozen=True)
class Product:
    name: str
    price_cents: int
```

<div class="text-sm mt-2"><code>@dataclass</code> gives you <code>__init__</code>, <code>__repr__</code> and <code>__eq__</code> for free. <code>frozen=True</code> makes it hashable, so a Product can be a dictionary key.</div>
</div>

<div class="px-3 py-2 rounded border border-orange-500/30 bg-orange-500/5">
<div class="font-bold text-orange-400 mb-1">Your job: <code>ShoppingCart</code></div>
<ul class="text-sm">
<li><code>add(product, quantity=1)</code>: <code>ValueError</code> if quantity &lt; 1</li>
<li><code>remove(product)</code>: removes it entirely; <code>KeyError</code> if absent</li>
<li><code>total_cents</code>: a property</li>
<li><code>__len__</code>: total number of units</li>
</ul>

<div class="mt-2 font-mono text-sm">uv run exercises/classes.py</div>
<div class="text-sm opacity-80">Expected: <code>3</code>, <code>1175</code>, then <code>1 275</code></div>
</div>

</div>

<!--
[1:07-1:15] Exercise 3.

- The cart stores `self._quantities: dict[Product, int]`. That only works because Product is frozen (hashable).
- add: validate quantity first, then `self._quantities[product] = self._quantities.get(product, 0) + quantity`.
- remove: `del self._quantities[product]` raises KeyError for free.
- total_cents: sum of price_cents * quantity. __len__: sum of quantities.
- The script also prints the Product itself first: Product(name='Coffee', price_cents=450). That's the free __repr__.
- Expected: 2 coffees + 1 bagel = 3 units, 2 x 450 + 275 = 1175 cents; after removing coffee: 1 unit, 275 cents.
-->
