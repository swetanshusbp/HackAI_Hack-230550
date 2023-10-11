from utils.calculation.calculation import calculation
from utils.calculation.convert import convert
from uagents import Context

class Display():
    def __init__(self,current_temp,feels_temp,msg):
        self.current_temp=current_temp
        self.feels_temp=feels_temp
        self.msg=msg
    def show(self):
        ctx:Context.logger.info("LMAO")
        ctx:Context.logger.info(f"Current Temperature is {self.current_temp:.2f}°C")
        print(f"Current Temperature is {self.current_temp:.2f}°C")
        ctx:Context.logger.info(f"Temperature feels like {self.feels_temp:.2f}°C")
        print(f"Temperature feels like {self.feels_temp:.2f}°C")
        ctx:Context.logger.info(self.msg)
        print(self.msg)
def display(current_temp,feels_temp,msg):
    return Display(current_temp=current_temp,feels_temp=feels_temp,msg=msg)
