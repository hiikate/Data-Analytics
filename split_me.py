# %% [markdown]
# A program that accepts a string in the format Age.FirstName and returns the value FirstName is Age years old

# %%
txt = input('Enter a string of Age.Firstname: ')

# %%
words = txt.split(".")
print(words)

# %%
age = words[0]
first_name = words[1]

# %%
print(f"{first_name} is {age} years old. Length of {first_name} is {len(first_name)}")


