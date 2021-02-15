import inspect


class class_one:
    def print_name():
        print("Hi I am class_one in file name1")

    print_name()

    def print_caller_info():
        # Get the full stack
        stack = inspect.stack()
        print(stack)
        previous_stack_frame = stack[-1]
        full_filename = previous_stack_frame.filename # Filename where caller lives
        filename = full_filename.split("\\")[-1]
        print(filename)
        # Get the module object of the caller
        # calling_module = inspect.getmodule(previous_stack_frame[0])
        # print(calling_module)
        # print(calling_module.__file__)

    print_caller_info()
