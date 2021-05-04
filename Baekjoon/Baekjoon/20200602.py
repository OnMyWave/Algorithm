def uppercase(obj):
    def wrapper(*args, **kwargs):
        print(f"Trace: calling {obj.__name__}()", end=" ")
        print(f"with{args}, {kwargs}")
        original_result = obj(*args, **kwargs)
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def intro(name, greeting):
    test = "py"
    return f"Hi, {name}, {greeting}"

 
print(intro("Mee", "Have a good time"))
