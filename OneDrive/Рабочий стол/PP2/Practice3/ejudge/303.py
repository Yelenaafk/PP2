def string_calculator(expr):
    to_int = {
        "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
        "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
    }
    to_str = {v: k for k, v in to_int.items()}
    for op in "+-*":
        if op in expr:
            left, right = expr.split(op)
            operator = op
            break
    def word_to_int(s):
        digits = ""
        for i in range(0, len(s), 3):
            digits += to_int[s[i:i+3]]
        return int(digits)
    def int_to_word(num):
        if num == 0:
            return "ZER"
        res = ""
        for d in str(num):
            res += to_str[d]
        return res
    a = word_to_int(left)
    b = word_to_int(right)
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    else:
        result = a * b
    return int_to_word(result)
print(string_calculator(input().strip()))