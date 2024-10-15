def input_int(text=""):
    while True:
        try:
            number = int(input(text))
            if number > 0:
                return number
            else:
                print("Please enter a number greater than 0")
                continue
        except ValueError:
            print("Please enter a number")
            continue
