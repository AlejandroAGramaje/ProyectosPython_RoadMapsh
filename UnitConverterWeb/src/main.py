def unit_converter(value, unit_from, unit_to):
    result = 0
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
        }
    }

    # Normalize unit names (lowercase)
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    # Convert Length
    if unit_from in conversions["Length"] and unit_to in conversions["Length"]:
        meters_value = value * conversions["Length"][unit_from]  # Convert to meters
        result = meters_value / conversions["Length"][unit_to]   # Convert from meters to target unit
        return round(result, 6)

    # Convert Weight
    elif unit_from in conversions["Weight"] and unit_to in conversions["Weight"]:
        kilograms_value = value * conversions["Weight"][unit_from]  # Convert to kilograms
        result = kilograms_value / conversions["Weight"][unit_to]   # Convert from kilograms to target unit
        return round(result, 6)

    # Convert Temperature
    elif unit_from in ["celsius", "fahrenheit", "kelvin"] and unit_to in ["celsius", "fahrenheit", "kelvin"]:
        return round(convert_temperature(value, unit_from, unit_to), 6)

    else:
        return "Invalid units"

# Temperature Conversion
def convert_temperature(value, unit_from, unit_to):
    if unit_from == "celsius":
        if unit_to == "fahrenheit":
            return (value * 9/5) + 32
        elif unit_to == "kelvin":
            return value + 273.15
    elif unit_from == "fahrenheit":
        if unit_to == "celsius":
            return (value - 32) * 5/9
        elif unit_to == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif unit_from == "kelvin":
        if unit_to == "celsius":
            return value - 273.15
        elif unit_to == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return "Invalid Temperature Units"
