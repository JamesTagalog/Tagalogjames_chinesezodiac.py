def chinese_zodiac(year):
    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"]
    start_year = 1924
    index = (year - start_year) % 12
    return animals[index]

year = int(input("Enter a year: "))
zodiac_sign = chinese_zodiac(year)
print(f"The Chinese zodiac sign for the year {year} is {zodiac_sign}.")