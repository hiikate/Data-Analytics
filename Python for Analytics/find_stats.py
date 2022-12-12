import numpy as np
import statistics as stats

arr = []
ch = int(input("Enter a number:"))
while(ch != 0):
    arr.append(ch)
    ch = int(input("Enter a number and '0' to end:"))

    print("\n**********STATS*******")

#finding mean
mean = np.mean(arr)
print(f"MEAN: {mean}")

# finding median
median = np.median(arr)
print(f"MEDIAN:{median}")

# finding mode
mode = stats.mode(arr)
print(f"MODE: {mode}")