'''
Write a function called validBraces that takes a string of braces, and determines if the order of the braces is valid. validBraces should return true if the string is valid, and false if it's invalid.

All input strings will be nonempty, and will only consist of open parentheses '(' , closed parentheses ')', open brackets '[', closed brackets ']', open curly braces '{' and closed curly braces '}'.

What is considered Valid?

A string of braces is considered valid if all braces are matched with the correct brace. For example:

'(){}[]' and '([{}])' would be considered valid, while '(}', '[(])', and '[({})](]' would be considered invalid.
'''
def validBraces(string):
    while '()' in string or '[]' in string or '{}' in string:# Eliminate all valid values
        string = string.replace('()','')
        string = string.replace('[]','')
        string = string.replace('{}','')
    return string == ''# If string are only composed by valid braces, final value should be empty


if __name__ == "__main__":
    print(validBraces( "(){}[]" ))