
from utils.api.call import call
from uagents import Model, Context, Agent

class WeatherAgent(Model,Context):
    def get_action(self, city_choice):
        Call = call(city_choice)
        data = Call.getdata()
        return data

def client():
    my_agent = WeatherAgent()
    return my_agent
