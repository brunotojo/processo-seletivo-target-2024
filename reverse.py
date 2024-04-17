def reverse(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

string = str(input('Enter string: '))

print(f'Reversed string: {reverse(string)}')
