from abc import ABC,abstractmethod
class Computer():
    @abstractmethod
    def process(self,app):
        pass
    def run(self,app):
        self.process(app)
class Laptop(Computer):
    def process(self, app):
        print(f"{app} processing using laptop")
class Mobile(Computer):
    def process(self, app):
        print(f"{app} proccinh using mobile")
dell=Laptop()
dell.run("Chrome")
dell.run("Pubg")


samsung=Mobile()
samsung.run("camera")
samsung.run("pubg")