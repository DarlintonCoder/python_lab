from utils import square, is_even, celsius_to_fahrenheit

n = int(input("Enter a number: "))

print("Square:", square(n))
print("Even:", is_even(n))
print("Fahrenheit:", celsius_to_fahrenheit(n))


from utils import greet

if __name__ == "__main__":
    print(greet("Developer"))