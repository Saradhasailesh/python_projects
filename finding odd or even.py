try: 
    n = int(input("Please enter a number:"))
    r = n % 2

    if r== 0:
        print("The number is an even number")

    else:
        print("The number is an odd number")    
except ValueError:
    print("Invalid input!Please enter a valid integer.")
