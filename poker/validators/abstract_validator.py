from abc import ABC, abstractmethod
from typing import List
from poker.card import Card


class AbstractValidator(ABC):
    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def valid_cards(self) -> List[Card]:
        pass
