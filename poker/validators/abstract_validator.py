from abc import ABC, abstractmethod
from typing import List
from poker.card import Card


class AbstractValidator(ABC):
    @abstractmethod
    def __init__(self, card: List[Card]) -> None:
        self._cards: List[Card]
        self._name: str

    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def valid_cards(self) -> List[Card]:
        pass
