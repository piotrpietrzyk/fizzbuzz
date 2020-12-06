def validate(start_value, end_value, prompt):
    while True:
        try:
            answer = int(input(f'Enter {prompt} range:'))
            assert start_value < answer < end_value
            return answer
        except ValueError:
            print("Enter an integer")
        except AssertionError:
            print(f"Enter an integer between {start_value+1} and {end_value-1}")