"""
    Program to convert celsius to Fahrenheit
"""
def celsius_to_far(Celsius):
    """ convert value given to fahhrenheit"""
    Fah = 25 * 9/5 + 32
    return Fah

def fah_to_cel(Fah):
    celsius = Fah - 32
    return celsius

celsius = 25
Fah = celsius_to_far(celsius)
print(f"{celsius} Degree is {Fah} Fahrenheit") 

celsius = fah_to_cel(Fah)
print(f"{Fah} Degree is {celsius} Celsius") 