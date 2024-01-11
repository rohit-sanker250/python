def exp_program(value):
    try:
        number=int(input(value))
        return number
    except ValueError:
        print("Error : invalid input,input a valid integer")
exp_program("abc")        
