"""Exercise 3: classes.

``Product`` is done: ``@dataclass`` writes ``__init__``, ``__repr__`` and
``__eq__`` for you, and ``frozen=True`` makes it hashable, so it can be a
dictionary key. Fill in the ``ShoppingCart`` TODOs, then run:

    uv run exercises/classes.py
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    """A product that can be added to a cart.

    Attributes:
        name: Display name of the product.
        price_cents: Unit price in cents (whole cents avoid rounding errors).
    """

    name: str
    price_cents: int


class ShoppingCart:
    """A shopping cart that tracks how many units of each product it holds."""

    def __init__(self) -> None:
        """Create an empty cart."""
        self._quantities: dict[Product, int] = {}

    def add(self, product: Product, quantity: int = 1) -> None:
        """Add ``quantity`` units of ``product`` to the cart.

        Args:
            product: The product to add.
            quantity: How many units to add. Must be at least 1.

        Raises:
            ValueError: If ``quantity`` is less than 1.
        """
        raise NotImplementedError("TODO")

    def remove(self, product: Product) -> None:
        """Remove ``product`` from the cart entirely.

        Args:
            product: The product to remove.

        Raises:
            KeyError: If ``product`` is not in the cart.
        """
        raise NotImplementedError("TODO")

    @property
    def total_cents(self) -> int:
        """Total price of everything in the cart, in cents."""
        raise NotImplementedError("TODO")

    def __len__(self) -> int:
        """Return the total number of units in the cart."""
        raise NotImplementedError("TODO")


if __name__ == "__main__":
    coffee = Product("Coffee", 450)
    bagel = Product("Bagel", 275)
    print(coffee)  # expected: Product(name='Coffee', price_cents=450)

    cart = ShoppingCart()
    cart.add(coffee, 2)
    cart.add(bagel)
    print(len(cart))  # expected: 3
    print(cart.total_cents)  # expected: 1175

    cart.remove(coffee)
    print(len(cart), cart.total_cents)  # expected: 1 275
