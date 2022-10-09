# python: count number of vowels in a string

string = input("Enter a string:")
vowels = 0

for i in string:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
        or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1

print("Total number of vowels in your string are", vowels)
