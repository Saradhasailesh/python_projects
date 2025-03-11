str = str(input("Please enter a word: "))

#for casesensitive string
str = str.casefold()

str1 = reversed(str)
print(list(str1))

if list(str1) == list(str):
    print(f"{str} is a palindrome")

else:
    print(f"{str} is not a palindrome")    




