"""Exercise 4: coding with AI (specify, generate, verify, explain).

1. Ask an AI assistant with a vague prompt: "Write a Python function that
   parses durations like 1h30m." Paste its answer in place of the stub, run

       uv run exercises/spec_first.py

   and compare the output with the expected values at the bottom.
2. Now give the AI the whole docstring below as the prompt. Paste, rerun,
   and compare again.
3. Explain every line to your neighbour. If you can't, you don't own it yet.
"""


def parse_duration(text: str) -> int:
    """Parse a duration such as "1h30m" into a whole number of minutes.

    Rules:
        - Hours ("2h"), minutes ("45m"), or both in that order ("1h30m").
        - Whole, non-negative numbers only ("1.5h" is invalid).
        - With an hours part, minutes must be below 60 ("1h90m" is invalid,
          but "90m" on its own is fine).
        - Units are case-insensitive. Spaces are allowed around the string
          and between the two parts ("1H 30m" is valid).
        - Anything else, including an empty string, is invalid.

    Args:
        text: The duration to parse.

    Returns:
        The total duration in minutes.

    Raises:
        ValueError: If ``text`` is not a valid duration.
    """
    raise NotImplementedError("TODO: paste the AI's answer here")


if __name__ == "__main__":
    # Expected: 90, 120, 45, 90, then ValueError for the last four.
    for text in ["1h30m", "2h", "45m", "1H 30m", "1h90m", "1.5h", "30m1h", ""]:
        try:
            print(f"{text!r:>9} -> {parse_duration(text)}")
        except ValueError:
            print(f"{text!r:>9} -> ValueError")
