"""Exercise 1: fill in the gradebook.

``Student`` is a dataclass: ``@dataclass`` writes ``__init__`` and
``__repr__`` for you. Fill in the three TODOs, then run:

    uv run exercises/gradebook.py

and compare the output with the expected values in the comments.
"""

from dataclasses import dataclass, field


def letter_grade(average: float) -> str:
    """Turn an average score into a letter grade.

    90 and above is an A, 80 and above a B, 70 and above a C, 60 and above
    a D, and anything lower an F.

    Args:
        average: An average score between 0 and 100.

    Returns:
        One of "A", "B", "C", "D" or "F".
    """
    raise NotImplementedError("TODO")


@dataclass
class Student:
    """A student and the scores they have earned so far.

    Attributes:
        name: The student's name.
        scores: Every score recorded, in order. ``field(default_factory=list)``
            gives each student their own new list.
    """

    name: str
    scores: list[float] = field(default_factory=list)

    def add_score(self, score: float) -> None:
        """Record a new score.

        Args:
            score: The score to record, between 0 and 100.

        Raises:
            ValueError: If ``score`` is below 0 or above 100.
        """
        raise NotImplementedError("TODO")

    @property
    def average(self) -> float:
        """The mean of all recorded scores, or 0.0 if there are none."""
        raise NotImplementedError("TODO")


if __name__ == "__main__":
    print(letter_grade(95), letter_grade(80), letter_grade(59.5))  # expected: A B F

    ada = Student("Ada")
    print(ada)  # expected: Student(name='Ada', scores=[])
    print(ada.average)  # expected: 0.0

    for score in (90, 85, 100):
        ada.add_score(score)
    print(ada.average, letter_grade(ada.average))  # expected: 91.66666666666667 A

    grace = Student("Grace")
    print(grace.scores)  # expected: []

    try:
        ada.add_score(120)
    except ValueError as error:
        print(f"ValueError: {error}")  # expected: ValueError: (your message)
