from collections import Counter

try: 

    a = str(input("Please enter a sentence:"))
    b = a.lower()
    # Calculate word frequencies using Counter
    w_freq = Counter(b.split())
    print(f"Word frequencies:")
    for word,count in w_freq.items():
        print(word, ":", count)

except Exception as e:
    print(f"An error occurred: {e}")  