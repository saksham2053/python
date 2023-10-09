class House:
    
    def __init__(self,name,color,garden=True,window=10):
        self.color=color
        self.name =name
        self.garden=garden
        self.window=window
    def set_color(self,color):
        self.color=color
    def __str__(self) -> str:
        return f"{self.name} kp ghar ho ani color chai{self.color} ho"
     
    
ram_ko_ghar=House("shyam","yellow",window=20)
print(ram_ko_ghar)
# print(ram_ko_ghar.color)
# print(ram_ko_ghar.garden)
# print(ram_ko_ghar.window)
        
# ram_ghar=House()
# print(ram_ghar.color)
# print(ram_ghar.window)
# shyam_color=House()
# shyam_color.set_color('green')
# print(shyam_color.color)
# sita_house=House()
# sita_house.set_color('white')
# print(sita_house.color)
