# -*- coding: utf-8 -*-

'''
NOTES:humanYears >= 1

Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that

Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
'''

def human_years_cat_years_dog_years(human_years):
    humanYears = human_years
    catYears = dogYears = 0
    if humanYears >= 1:
        humanYears = humanYears - 1
        catYears = dogYears = 15
        if humanYears == 0:
            return [human_years,catYears,dogYears]
        for i in range(humanYears, 0, -1):
            if i == 1:
                catYears += 9
                dogYears += 9
            else:
                catYears += 4
                dogYears += 5
    return [human_years,catYears,dogYears]

if __name__ ==  "__main__":
    print(human_years_cat_years_dog_years(1) == [1,15,15])
    print(human_years_cat_years_dog_years(2) == [2,24,24])
    print(human_years_cat_years_dog_years(10) == [10,56,64])