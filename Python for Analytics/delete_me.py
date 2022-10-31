# %%
import os
print ("Enter 'quit' for existing the program")
filename = input("about_me.txt")
if filename == 'quit':
    exit()
else:
    print ('\nStarting the removal of the file!')
    os.remove('about_me.txt')

    print ('\nFile about_me', filename, 'is successful deleted!')


