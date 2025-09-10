conversion = {"I":1,
              "V":5,
              "X":10,
              "L":50,
              "C":100,
              "D":500,
              "M":1000
              }

def parse_roman_numeral(numeral: str):
    numeral = numeral.upper()
    wrong_chars = [char for char in numeral if char not in conversion]
    if wrong_chars:
        print("Enter the correct Roman Numerals ")
        return
    number = 0
    i = 0
    while i < len(numeral):
        if i <= len(numeral)-2 and conversion.get(numeral[i]) < conversion.get(numeral[i+1]):
            number = number + (conversion.get(numeral[i+1]) - conversion.get(numeral[i]))
            i = i+2
            continue
        number = number + conversion.get(numeral[i])
        i = i+1
    print(number)

parse_roman_numeral("ix")