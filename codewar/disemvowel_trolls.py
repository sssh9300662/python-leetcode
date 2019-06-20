def disemvowel(string):
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        string = string.replace(vowel, '')

    return string


if __name__ == "__main__":
    print(disemvowel("This website is for losers LOL!"))
