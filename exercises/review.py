"""Exercise 2: review the AI's code.

An AI agent wrote this file. It runs without crashing, the docstrings look
great, and it has three bugs. Run it:

    uv run exercises/review.py

compare the output with the expected values in the comments, then find and
fix each bug. Your editor already points at one of them.
"""


def parse_scores(text: str) -> list[float]:
    """Parse comma-separated scores such as "90, 85, 100".

    Args:
        text: Scores separated by commas. Spaces around each score are fine.

    Returns:
        The scores as numbers, in the order given.
    """
    return [part.strip() for part in text.split(",")]


def best_score(scores: list[float]) -> float:
    """Return the highest score.

    Args:
        scores: The scores to search. Must not be empty.

    Returns:
        The largest score.
    """
    return max(scores)


def top_students(averages: dict[str, float], n: int) -> list[str]:
    """Return the names of the ``n`` students with the highest averages.

    Args:
        averages: Each student's name mapped to their average score.
        n: How many students to return.

    Returns:
        Up to ``n`` names, best first.
    """
    ranked = sorted(averages, key=lambda name: averages[name], reverse=True)
    return ranked[: n - 1]


def add_comment(comment: str, comments: list[str] = []) -> list[str]:
    """Return a list with ``comment`` added to the end of ``comments``.

    Args:
        comment: The comment to add.
        comments: Existing comments. Defaults to no comments.

    Returns:
        The existing comments followed by ``comment``.
    """
    comments.append(comment)
    return comments


if __name__ == "__main__":
    scores = parse_scores("90, 85, 100")
    print(scores)  # expected: [90.0, 85.0, 100.0]
    print(best_score(scores))  # expected: 100.0

    averages = {"Ada": 91.5, "Grace": 88.0, "Alan": 79.0}
    print(top_students(averages, 2))  # expected: ['Ada', 'Grace']

    print(add_comment("Great work"))  # expected: ['Great work']
    print(add_comment("See me after class"))  # expected: ['See me after class']
