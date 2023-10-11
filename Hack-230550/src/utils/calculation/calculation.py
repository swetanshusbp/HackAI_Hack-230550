class Calculation:
    def __init__(self,low,high,temp):
        self.low=low
        self.high=high
        self.temp=temp
    def check(self):
        if(self.temp<self.low):
            return f"Current Temperature is lower than your minimum preferred temperature by {(self.low-self.temp):.2f}°C"
        elif(self.temp>self.high):
            return f"Current Temperature is higher than your maximum preferred temperature by {(self.temp-self.high):.2f}°C"
        else:
            return "Current Temperature is within your preferred range"
def calculation(low,high,temp):
    return Calculation(low,high,temp)