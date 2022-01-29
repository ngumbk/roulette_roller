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


match = re.findall(r'P:\w+\W', line)
predictions_array = []
for item in match:
    predictions_array.append(item[2:len(item) - 1])

match = re.findall(r'W:\w+\W', line)
colors_won_array = []
for item in match:
    colors_won_array.append(item[2:len(item) - 1])

wins = 0
for index, prediction in enumerate(predictions_array):
    if prediction == colors_won_array[index]:
        wins += 1

print(f"Games: {len(predictions_array)}, true predictions: {wins}. \n Wins/predictions: {wins/len(predictions_array)}")

