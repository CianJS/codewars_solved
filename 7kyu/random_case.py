# -*- coding: utf-8 -*-

"""
Write a function that will randomly upper and lower characters in a string - randomCase() (random_case() for Python).

A few examples:
    randomCase("Lorem ipsum dolor sit amet, consectetur adipiscing elit") == "lOReM ipSum DOloR SiT AmeT, cOnsEcTEtuR aDiPiSciNG eLIt"

    randomCase("Donec eleifend cursus lobortis") == "DONeC ElEifEnD CuRsuS LoBoRTIs"

Note: this function will work within the basic ASCII character set to make this kata easier - so no need to make the function multibyte safe.
"""

def random_case(x):
    import random
    result = ''
    for i in x:
        if random.randrange(0,2):
            result += i.upper()
        else:
            result += i.lower()
    return result

if __name__ == "__main__":
    v = [
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
      "Donec eleifend cursus lobortis",
      "THIS IS AN ALL CAPS STRING",
      "this is an all lower string"
    ]

    random = random_case(v)
    print random
