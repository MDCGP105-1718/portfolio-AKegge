def fizzbuzz(low, high):
    for n in range (low, high, 1):
        if(n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz")
        elif(n % 3 == 0):
            print("Fizz")
        elif(n % 5 == 0):
            print("Buzz")
        else:
            print(n)

high = input("Please enter a high value: ")
low = input("Please enter a low value: ")
fizzbuzz(int(low), int(high))
