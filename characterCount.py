string = "This is a Python program"
char_count = dict()
for i in string:
    char_count[i] = char_count.get(i, 0) + 1  # Increment count
    
print(char_count)

    