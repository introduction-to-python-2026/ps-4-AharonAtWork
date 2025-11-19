def split_before_each_uppercases(formula):
        split_formula = []
    start = 0
    for end in range(1, len(formula)):
        if formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end
    
    # Append the last part of the string
    if formula:
        split_formula.append(formula[start:len(formula)])
    
    return split_formula


def split_at_first_digit(formula):
    first_digit_index = -1  # Initialize to -1 to indicate no digit found yet

    # Loop through characters starting from the second character (index 1)
    for i in range(1, len(formula)):
        if formula[i].isdigit():
            first_digit_index = i
            break  # Digit found, stop the loop

    # Check if a digit was found in the searched range (from index 1 onwards)
    if first_digit_index == -1:
        # If no digit was found, return the original formula and the number 1
        return formula, 1
    else:
        # If a digit was found, split the formula
        prefix = formula[:first_digit_index]
        numeric_part = int(formula[first_digit_index:])
        return prefix, numeric_part
