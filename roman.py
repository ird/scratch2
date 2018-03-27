"""
rton(numeral) - roman to number
returns the number represented by the roman numeral string provided
e.g rton("MCMXI") = 1911
"""
def rton(numeral):
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sub_not_tbl = {('I', 'V'): 4, ('I', 'X'): 9, ('X', 'L'): 40, ('X', 'C'): 90,
                   ('C', 'D'): 400, ('C', 'M'): 900}
    result = 0
    sub_notation = False
    for char in numeral:
        if not sub_notation:
            # in the most common case, just add the value of the numeral
            result += table[char]
            prev_ch = char
            # if the character could be used in subtractive notation, flag it to check
            if char in ['I', 'X', 'C']:
                sub_notation = True
        else:
            # we've reached here because the last character could be used as a subtractive
            if((prev_ch, char) in sub_not_tbl):
                result += sub_not_tbl[(prev_ch, char)]
                result -= table[prev_ch]
            else:
                # the previous char was not used in subtractive notation
                result += table[char]
            sub_notation = False
    return result
        
print("MDCCLXXVI =", rton("MDCCLXXVI"))
