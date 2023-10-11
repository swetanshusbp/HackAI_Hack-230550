from agents.client.client import client
from agents.display.display import display
from utils.calculation.calculation import calculation
from utils.calculation.convert import convert
from uagents import Bureau

bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)

def main():
    #User Input
    city = input("Enter your target city: ")
    low = eval(input("Enter your lowest preferred temperature in Celsius: "))
    high = eval(input("Enter your highest preferred temperature in Celsius: "))
    
    #fetching weather data
    Client = client()
    data =  Client.get_action(city)
    
    #formatting data for temperature
    current_temp = data['main']['temp']
    feels_temp = data['main']['feels_like']
    
    #changing kelvin to celsius
    Convert1 = convert(current_temp)
    current_temp = Convert1.convert()
    Convert2 = convert(feels_temp)
    feels_temp = Convert2.convert()
    
    #Checking if current temperature is in threshold of user temperature choice
    Calculation = calculation(low,high,current_temp)
    result = Calculation.check()
    
    #Displaying the final results
    Display = display(current_temp,feels_temp,result)
    Display.show()
    
if __name__=="__main__":
    main()
    
    