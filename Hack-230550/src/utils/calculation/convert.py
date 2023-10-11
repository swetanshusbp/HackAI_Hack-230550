class Convert:
    def __init__(self,temp):
        self.temp = temp
    def convert(self):
        return self.temp-273.15

def convert(temp):
    return Convert(temp)