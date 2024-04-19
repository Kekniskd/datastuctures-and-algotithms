import re


def extract_names(formula_str):
    # Define regex pattern for extracting names
    pattern = r'[a-zA-Z\s]+'
    # Find all names in the formula using regex pattern
    formula_list = re.findall(pattern, formula_str)

    return formula_list


# Example usage:
formula = "Premium Home Buildings * (Premium Home Contents + Premium Home Valuables) + Premium Domestic Animals + Premium Prop Damage - Premium Frozen Food + Premium Livestock Non Disease + Premium Livestock Disease / 20"
names = extract_names(formula)
print(names)
