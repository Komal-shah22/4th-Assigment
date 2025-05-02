
def double_numbers(numbers):
    return [num * 2 for num in numbers]

def main():
    numbers = [1, 2, 3, 4]
    doubled = double_numbers(numbers)
    print("Doubled list:", doubled)

if __name__ == '__main__':
    main()
