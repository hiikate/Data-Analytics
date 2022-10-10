# %% [markdown]
# A program that contains a lambda expression that converts Fahrenheit  to Celsius. Accept the Fahrenheit temperature and display the Celsius result using the lamba. The formula is: C = 5/9 * (F-32)

# %%
lambda F: 5.0/9.0 * (F-32)
F = int(input("Enter a temp in Fahrenheit: "))
C = 5.0/9.0 * (F-32)
print ("Temperature:", F, "Fahrenheit =", C, "Celsius")


