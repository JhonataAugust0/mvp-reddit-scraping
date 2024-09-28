from abc import ABC, abstractmethod


class StoragePort(ABC):
    @abstractmethod
    def save_to_csv(data, filename):
        pass

    @abstractmethod
    def save_to_json(data, filename):
        pass
