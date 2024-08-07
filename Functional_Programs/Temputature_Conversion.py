'''@Author: Venkatesh
@Date: 2024-08-03 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
class Temperature:
    @staticmethod
    def temperature_conversion(temperature, to_scale):
        if to_scale.lower() == 'celsius':
            return (temperature - 32) * 5 / 9
        elif to_scale.lower() == 'fahrenheit':
            return (temperature * 9 / 5) + 32
        else:
            raise ValueError("to_scale must be either 'Celsius' or 'Fahrenheit'")
def main():
    temperature=int(input("Enter Temperature:"))
    to_scale=str(input("Eneter celsius Or fehrenheit:"))
    print(Temperature.temperature_conversion(temperature,to_scale))
main()