# main.py

def unit_converter(value, unit_from, unit_to):
    conversions = {
        "Length": {
            "millimeter": 0.001,
            "centimeter": 0.01,
            "meter": 1,
            "kilometer": 1000,
            "inch": 0.0254,
            "foot": 0.3048,
            "yard": 0.9144,
            "mile": 1609.34
        },
        "Weight": {
            "milligram": 0.000001,
            "gram": 0.001,
            "kilogram": 1,
            "ounce": 0.0283495,
            "pound": 0.453592
        },
        "Temperature":{
            "celsius": 0,
            "kelvin": 273.15,
            "fahrenheit": 32
        }
    }