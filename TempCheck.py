class Temperature:
    def __init__(self, city, temp):
        self.city = city
        self.temp = temp
        
    def check_temp(self):
        if self.temp >= 35:
            return "It's a Hot Day"
        elif self.temp <=22:
            return "It's a Cold Day"    
        else:
            return "It's a normal Day"

MyCity = input("Enter your City: ")
MyTemp = int(input("Enter your Temperature: "))
temp = Temperature(MyCity, MyTemp)
print(temp.check_temp())
    
