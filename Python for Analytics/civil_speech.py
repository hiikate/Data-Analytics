# %%
try:
    with open ("gettysburg.txt") as f:
        text = f.read()
except FileNotFoundError:
    text = None

print(text)

f.close()

pass


