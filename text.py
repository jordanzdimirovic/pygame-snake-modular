my_variable = 5

def my_function():
    global my_variable
    my_variable = 10
    print(f"In function: {my_variable}")

if __name__ == "__main__":
    my_function()
    print(f"Outside function: {my_variable}")