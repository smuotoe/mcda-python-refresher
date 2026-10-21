"""Live demo: what type hints and a docstring buy you in VS Code.

Open this file in VS Code and follow the steps in the slide's speaker notes:
hover over ``average``, type ``result.``, then add the hints and docstring
and try again.

    uv run demos/type_hints.py
"""


def average(scores, drop_lowest=False):
    if drop_lowest and len(scores) > 1:
        scores = sorted(scores)[1:]
    return sum(scores) / len(scores)


if __name__ == "__main__":
    result = average([90, 85, 100])
    print(result)
