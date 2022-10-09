# %% [markdown]
# The program accepts two integer values as arguments and returns the value that is the greater of the two. For example, if 7 and 12 are passed as arguments to the function, the function should return 12.

# %%
def max (firstNumber, secondNumber ):
    if firstNumber > secondNumber:
        return firstNumber
    return secondNumber

# %% [markdown]
# Promtp users to enter two integer values

# %%
firstNumber = int(input("Input the first number: "))
secondNumber = int(input("Input the second number: "))

# %% [markdown]
# Get the max value

# %%
maxValue = max(firstNumber, secondNumber)

# %% [markdown]
# Display the great number as result

# %%
print(f"The Max value is {maxValue}")


