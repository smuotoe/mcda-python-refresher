"""Exercise 1: functions.

Fill in the TODOs, then run:

    uv run exercises/functions.py

and compare the output with the expected values in the comments.
"""


def slugify(title: str) -> str:
    """Turn a title into a URL slug: "Hello, World!" becomes "hello-world".

    Lowercase the text, replace every run of characters that aren't letters
    or digits with a single "-", and strip "-" from both ends.

    Args:
        title: Any text, such as a blog post title.

    Returns:
        The slug.
    """
    raise NotImplementedError("TODO")


def add_tag(tag: str, tags: list[str] = []) -> list[str]:
    """Return a new list with ``tag`` added to the end of ``tags``.

    TODO: this version has a bug. Run the file, look at the second call,
    then fix it (hint: default to None, and don't modify the caller's list).

    Args:
        tag: The tag to add.
        tags: Existing tags. Defaults to no tags.

    Returns:
        A new list with the existing tags followed by ``tag``.
    """
    tags.append(tag)
    return tags


def chunk[T](items: list[T], size: int) -> list[list[T]]:
    """Split ``items`` into chunks of length ``size``; the last may be shorter.

    Args:
        items: The items to split.
        size: Maximum length of each chunk. Must be at least 1.

    Returns:
        The chunks, in order.

    Raises:
        ValueError: If ``size`` is less than 1.
    """
    raise NotImplementedError("TODO")


if __name__ == "__main__":
    print(add_tag("python"))  # expected: ['python']
    print(add_tag("uv"))  # expected: ['uv']
    print(slugify("Hello, World!"))  # expected: hello-world
    print(slugify("Python 3.13: What's New?"))  # expected: python-3-13-what-s-new
    print(chunk([1, 2, 3, 4, 5], 2))  # expected: [[1, 2], [3, 4], [5]]
