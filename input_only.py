def input_int(text=""):
    while True:
        try:
            number = int(input(text))
            if number > 0:
                return number
        except ValueError:
            pass

def input_yes_no(text=""):
    while True:
        try:
            answer = input(text)
            if answer in ["yes", "no"]:
                return answer
        except ValueError:
            pass



