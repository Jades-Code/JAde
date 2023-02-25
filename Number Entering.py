numbers = []  


while True:
    
    num_str = input("Enter a number (or 'done' to exit): ")
    
    if num_str == "done":
        break
    
    
    try:
        num = float(num_str)
        numbers.append(num)
    except ValueError:
        print("Invalid input, please enter a number or 'done' to exit.")


print("Numbers entered: ", numbers)


if len(numbers) > 0:
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    
    print("Sum: ", total)
    print("Average: ", average)
    print("Maximum: ", maximum)
    print("Minimum: ", minimum)
else:
    print("No numbers entered.")
