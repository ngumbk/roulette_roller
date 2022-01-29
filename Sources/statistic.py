import re
import matplotlib.pyplot as plt
import numpy as np


def makeStatistic(name, filename):
    file = open(filename, 'r')
    line = file.read()
    file.close()

    match = re.findall(r'BAL:\W*\d+.\d+', line)
    balance_value_array = []
    time_array = []
    for index, item in enumerate(match):
        balance_value_array.append(float(item[4:len(item)]))
        time_array.append((index + 1) * 10)

    plt.title(name)
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

    print(f"{name}\nGames: {len(predictions_array)}, true predictions: {wins}. \n Wins/predictions: {wins/len(predictions_array)}\n")


makeStatistic("Ставка на меньший", '../Data/newresult_1_bet.txt')
makeStatistic("Рандом", '../Data/newresult_3_bet.txt')
