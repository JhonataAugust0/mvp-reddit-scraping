from abc import ABC, abstractmethod


class StoragePort(ABC):
    @abstractmethod
    def save_to_csv(data: dict, filename: str) -> None:
        pass

    @abstractmethod
    def save_to_json(data: dict, filename: str) -> None:
        pass
