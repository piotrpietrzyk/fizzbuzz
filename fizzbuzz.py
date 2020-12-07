def validate(start_value, end_value, prompt):
    while True:
        try:
            answer = int(input(f'Enter {prompt} range: '))
            assert start_value < answer < end_value
            return answer
        except ValueError:
            print("Enter an integer")
        except AssertionError:
            print(f"Enter an integer between {start_value+1} and {end_value-1}")


if __name__ == '__main__':
    start = validate(0, 10000, "start")
    end = validate(start, 10001, "end")
    for i in range(start, end+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)
