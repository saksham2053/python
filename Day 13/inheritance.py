class Granfather:
    def __init__(self) -> None:
        print("granfather has luxary house")
    house="luxary house"
class Father(Granfather):
    def __init__(self) -> None:
        print('now father has 3bhk house.')
        super().__init__()
    car="ferrari"
class Mother:
    jwaellary='gold'
class Son(Father,Mother):
    def __init__(self) -> None:
        print('bought two houses.')
        
        super().__init__()
    electronic="PS5"
son =Son()
father=Father()
print(isinstance(son,object))
# print(son.car)
# print(son.house)
# print(son.jwaellary)
