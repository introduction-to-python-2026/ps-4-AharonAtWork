def split_before_each_uppercases(formula):
    if not formula:
        return []
    
    split_formula = []
    start = 0
    for end in range(1, len(formula)):
        if formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end
    split_formula.append(formula[start:])
    return split_formula


def split_at_first_digit(formula):
    for i, char in enumerate(formula):
        if char.isdigit():
            prefix = formula[:i]
            numeric_part = int(formula[i:])
            return prefix, numeric_part
    return formula, 1
