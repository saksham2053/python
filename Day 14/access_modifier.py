class Person:
    def __init__(self) -> None:
        self.name="ram"
        self._age=12 #protected
        self.__phn_number="91233456789" #private
    def get_phn_number(self):
        return self.__phn_number
    def det_phn_numb(self,change):
        self.__phn_number= change
    change=property(det_phn_numb,get_phn_number)
        
        
p=Person()
p.det_phn_numb('12345')
print(p.get_phn_number())