# %% [markdown]
# A program that asks a person their age. Accept an int. Use a custom exception to return a message if the number entered is an int that is less than 1 or greater than 115. Create an exception that catches an error if a non int is entered. 

# %%
# creating an exceptions class
class AgeOutOfRange(Exception):
    """Raised when the input value is either too small or too big"""
    pass


while True:
    try: 
        age = input("Please enter your age: ")
        if not age.isConvertableToInt():
            print("Not valid integer.")
        age = int(age)
        if age < 1 or age > 115:
            raise AgeOutOfRange(f"Age must be between 1 and 115: {age}")
        break
    except ValueError:
        print("No valid integer! Try again")

print(f"Great, you entered an integer: {age}")


