from abc import abstractmethod


class Repository:
    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_one(self, id):
        pass

    @abstractmethod
    def create(self, dto):
        pass

    @abstractmethod
    def update(self, id, dto):
        pass

    @abstractmethod
    def delete(self, id):
        pass
