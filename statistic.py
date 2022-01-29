import re
import matplotlib.pyplot as plt

file = open('results.txt', 'r')
line = file.read()
file.close()

match = re.findall(r'BAL:\d+.\d+;', line)
balance_value_array = []
time_array = []
for index, item in enumerate(match):
    balance_value_array.append(item[4:len(item) - 1])
    time_array.append((index + 1) * 10)

plt.title("Balance to time")
plt.xlabel("time")
plt.ylabel("Balance")
plt.grid()

plt.plot(time_array, balance_value_array)
plt.show()

print(balance_value_array, '\n', time_array)
